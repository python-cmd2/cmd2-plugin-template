#
# -*- coding: utf-8 -*-

import functools
from typing import Callable

def myplugin_decorator(func: Callable) -> Callable:
    """An empty decorator for myplugin"""
    #@functools.wraps(func)
    def _myplugin_decorator(self, *args, **kwargs):
        self.poutput("in the myplugin decorator")
        func(self, *args, **kwargs)
    _myplugin_decorator.__doc__ = func.__doc__
    return _myplugin_decorator

class MypluginMixin:
    """A mixin class which adds methods to a cmd2 subclass"""
    def do_myplugin(self, arg):
        """Add a myplugin command to cmd2"""
        self.poutput("just ran my plugin command")
