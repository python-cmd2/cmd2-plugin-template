#
# coding=utf-8

from cmd2 import cmd2
import cmd2_myplugin

class PluginExample(cmd2.Cmd, cmd2_myplugin.SayMixin):
    """An class to show how to use a plugin"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @cmd2_myplugin.empty_decorator
    def do_something(self, arg):
        self.poutput(arg)

if __name__ == '__main__':
    app = PluginExample()
    app.cmdloop()
