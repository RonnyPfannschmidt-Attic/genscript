from genscript.pkgpacker import generate_script

script = generate_script(
    entry='import py;py.test.cmdline.main()',
    packages=['py', 'pytest'],
)

with open('script.py', 'w') as f:
    f.write(script)
