import py
import pickle
import zlib
import base64

def find_toplevel(name):
    for syspath in py.std.sys.path:
        base = py.path.local(syspath)
        lib = base/name
        if lib.check(dir=1):
            return lib
        mod = lib + '.py'
        if mod.check(file=1):
            return mod
    raise LookupError(name)

def pkgname(toplevel, rootpath, path):
    parts = path.parts()[len(rootpath.parts()):]
    return '.'.join([toplevel] + [x.purebasename for x in parts])

def pkg_to_mapping(name):
    toplevel = find_toplevel(name)
    if toplevel.check(file=1):
        return {name: toplevel.read()}

    name2src = {}
    for pyfile in toplevel.visit('*.py'):
        pkg = pkgname(name, toplevel, pyfile)
        name2src[pkg] = pyfile.read()
    return name2src


def compress_mapping(mapping):
    data = pickle.dumps(mapping, 2)
    data = zlib.compress(data, 9)
    data = base64.encodestring(data)
    data = data.decode('ascii')
    return data


def compress_packages(names):
    mapping = {}
    for name in names:
        mapping.update(pkg_to_mapping(name))
    return compress_mapping(mapping)


def generate_script(entry, packages):
    data = compress_packages(packages)
    tmpl = py.path.local(__file__).dirpath().join('standalonetemplate.py')
    exe = tmpl.read()
    exe = exe.replace('@SOURCES@', data)
    exe = exe.replace('@ENTRY@', entry)
    return exe


def pytest_addoption(parser):
    group = parser.getgroup("debugconfig")
    group.addoption("--genscript", action="store", default=None,
        dest="genscript", metavar="path",
        help="create standalone py.test script at given target path.")

def pytest_cmdline_main(config):
    genscript = config.getvalue("genscript")
    if genscript:
        script = generate_script(
            'import py; py.test.cmdline.main()',
            ['py', 'pytest'],
        )

        genscript = py.path.local(genscript)
        genscript.write(script)
        return 0
