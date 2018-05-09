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

class SayMixin:
    """A mixin class which adds a 'say' command to a cmd2 subclass"""
    def do_say(self, arg):
        """Simple say command"""
        self.poutput("just ran the say command from a plugin")
