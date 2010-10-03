Module Maker
=============

Summary
-------

The module maker addsmetadata you'd pass to setup()
or enter into the [metadata] section
to a copy of the vanilla module and supplies it as source distribution
for uploading to pypi.

Mechanism
---------

In order to create the source distribution file it will walk the source file
till it finds the comment `# Insert Genscript Metadata Here`.
after that it will put simple assignments for
version, homepage, author.

The result will be stored in `$distdir/$name-$version.py`.
If the distutils/distutils2 command is used the file is added as upload target
