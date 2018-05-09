#
# -*- coding: utf-8 -*-

import cmd2
import cmd2_myplugin

class PluginExample(cmd2.cmd2.Cmd, cmd2_myplugin.MypluginMixin):
    """An class to show how to use a plugin"""
    def __init__(self):
        super().__init__()

    @cmd2_myplugin.myplugin_decorator
    def do_something(self, arg):
        self.poutput(arg)

if __name__ == '__main__':
    app = PluginExample()
    app.cmdloop()
