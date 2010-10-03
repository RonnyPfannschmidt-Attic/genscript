import py
from genscript.module_maker import update_script

def test_update_script():
    source = py.code.Source("""
    def fun():
        pass

    # Genscript Metadata
    """)
    result = update_script(str(source), dict(version='1.3'))
    print result
    assert "\nversion = '1.3'\n" in result

def test_update_fails_for_missing():
    py.test.raises(ValueError, update_script, 'test_line\n', {})




