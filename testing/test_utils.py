from genscript.utils import distribution_metadata
import py

def pytest_generate_tests(metafunc):
    metafunc.addcall(id='ds1', param='distutils.core')
    metafunc.addcall(id='ds2', param='distutils2.core')

def pytest_funcarg__dist_class(request):
    mod = py.test.importorskip(request.param)
    return mod.Distribution

def test_metadata(dist_class):
    input = {
        'version': '1.0',
        'author': 'Test',
        'author_email': 'test@example.com'
    }

    dist = dist_class(input)
    extracted = distribution_metadata(dist.metadata)
    assert extracted == {
        'version': '1.0',
        'author': 'Test <test@example.com>',
        'url': None,
        'maintainer': None,
    }
