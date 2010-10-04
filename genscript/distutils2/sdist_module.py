
from distutils2.command.cmd import Command
from genscript.module_maker import SdistModuleMixin


class sdist_module(SdistModuleMixin, Command):
    pass
