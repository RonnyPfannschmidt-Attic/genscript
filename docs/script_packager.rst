Script Packager
===============

Summary
-------

The Script Packager turns a python script + its dependencies into a single python script
including a metadata header to tell the distributions and some of their metadata.

It can be used to ship single script version of more complex packages/scripts.


Mechanism
---------

The Script packager collects python source as well as limited distribution metadata,
compresses them and ships them with a pep 302 based loader inside of single python script,
which decompresses the packages, makes them importable via the loader 

It also fakes enough egg metadata to make entrypoints usefull.

After this setup is done it invokes the main entrypoint of the script.
