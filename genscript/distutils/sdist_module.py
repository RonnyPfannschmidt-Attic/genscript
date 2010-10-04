
from distutils.cmd import Command
from genscript.module_maker import SdistModuleMixin


class sdist_module(SdistModuleMixin, Command):
    def __init__(self, dist):
        Command.__init__(self, dist)
        SdistModuleMixin.__init__(self, dist)
