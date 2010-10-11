from genscript.pkgpacker import generate_script

with open('script.py', 'w') as f:
    f.write(generate_script(None, ['py', 'pytest']))
