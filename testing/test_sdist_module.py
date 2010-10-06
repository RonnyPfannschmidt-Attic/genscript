from distutils.dist import Distribution
from genscript.module_maker import SdistModuleMixin


def test_sdist_module(tmpdir):
    script = tmpdir.join('test.py')
    script.write('# Genscript Metadata')

    cmd = SdistModuleMixin()
    dist = cmd.distribution=Distribution({'version': '1.0'})

    sdist = dist.get_command_obj('sdist')
    sdist.ensure_finalized()
    sdist.dist_dir = str(tmpdir)

    dist.dist_files=[]
    dist.version=1.0
    cmd.initialize_options()
    cmd.module = str(script)
    cmd.finalize_options()
    cmd.run()
    assert dist.dist_files ==[('sdist_module', '', 'test-1.0.py')] #XXX
    
    assert tmpdir.join('test-1.0.py').check()

    new_content = tmpdir.join('test-1.0.py').read()
    assert 'version' in new_content



