import py

def find_toplevel(name):
    for syspath in py.std.sys.path:
        base = py.path.local(syspath)
        lib = base/name
        if lib.check(dir=1):
            return lib
    raise LookupError(name)

def pkgname(toplevel, rootpath, path):
    parts = path.parts()[len(rootpath.parts()):]
    return '.'.join([toplevel] + [x.purebasename for x in parts])

def pkg_to_mapping(name):
    toplevel = find_toplevel(name)
    name2src = {}
    for pyfile in toplevel.visit('*.py'):
        pkg = pkgname(name, toplevel, pyfile)
        name2src[pkg] = pyfile.read()
    return name2src
