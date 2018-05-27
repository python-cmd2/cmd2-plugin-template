#
# coding=utf-8

import sys

import functools
from typing import Callable

def empty_decorator(func: Callable) -> Callable:
    """An empty decorator for myplugin"""
    @functools.wraps(func)
    def _empty_decorator(self, *args, **kwargs):
        self.poutput("in the empty decorator")
        func(self, *args, **kwargs)
    _empty_decorator.__doc__ = func.__doc__
    return _empty_decorator


class MyPlugin:
    """A mixin class which adds a 'say' command to a cmd2 subclass

    The order in which you add the mixin matters. Say you want to
    use this mixin in a class called MyApp.

    class MyApp(cmd2_myplugin.MyPlugin, cmd2.Cmd):
        def __init__(self, *args, **kwargs):
            # gotta have this or neither the plugin or cmd2 will initialize
            super().__init__(*args, **kwargs)
    """
    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2 initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2 initializes
        # this is where you register any hook functions
        self.register_preloop_hook(self.preloop_hook)
        self.register_postloop_hook(self.postloop_hook)
        self.register_postparsing_hook(self.postparsing_hook)

    def do_say(self, statement):
        """Simple say command"""
        self.poutput(statement)

    #
    # define hooks as functions, not methods
    def preloop_hook(self):
        """Method to be called before the command loop begins"""
        self.poutput("preloop hook")

    def postloop_hook(self):
        """Method to be called after the command loop finishes"""
        self.poutput("postloop hook")

    def postparsing_hook(self, statement):
        """Method to be called after parsing user input, but before running the command"""
        self.poutput('in postparsing_hook')
        return False, statement
