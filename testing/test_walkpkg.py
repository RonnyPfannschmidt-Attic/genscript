import py
from genscript.pkgpacker import find_toplevel, pkgname, pkg_to_mapping
from genscript import pkgpacker

py_pkg = py.path.local(py.__file__).pypkgpath()

@py.test.mark.skipif(py_pkg is None, reason='magical pylib import')
def test_find_toplevel():
    pylib = find_toplevel('py')
    assert pylib == py_pkg


def test_pkgname(tmpdir):
    result = pkgname('test', tmpdir, tmpdir/'foo.py')
    assert result == 'test.foo'


def test_pkg_to_mapping(tmpdir, monkeypatch):
    monkeypatch.setattr(pkgpacker, 'find_toplevel', lambda x:tmpdir)
    tmpdir.join('test.py').write('#test\n')
    tmpdir.join('__init__.py').write('#!/bin/python')

    mapping = pkg_to_mapping('test')
    expected = {
        'test.__init__': '#!/bin/python',
        'test.test': '#test\n',
    }
    assert mapping == expected

