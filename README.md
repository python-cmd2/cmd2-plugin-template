# Creating a plugin for cmd2

## Using this template

This template assumes you are creating a new cmd2 plugin called `myplugin`. I
expect you will want to give your plugin a different name. You will need to
rename some of the files and directories in this template to your own package
name. Don't forget to modify the imports and `setup.py`.

You'll probably also want to rewrite the README :)

## Naming

You should prefix the name of your project with `cmd2-`. Within that project,
you should have a package with a prefix of `cmd2_`.

## How to add functionality to cmd2

There are several ways to add functionality to `cmd2` using a plugin.

### Initialization

You can create a mixin class which adds commands to a `cmd2` subclass.

Your mixin needs to include the following:

```python
class MyPlugin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

and it must be mixed in by:

```python
class Example(cmd2_myplugin.MyPlugin, cmd2.Cmd):
    """An class to show how to use a plugin"""
    def __init__(self, *args, **kwargs):
        print("pluginexample init")
        super().__init__(*args, **kwargs)
```

Note how the plugin must be inherited before `cmd2.Cmd`. This is required for two reasons:

- As of python 3.6.5, the `cmd.Cmd.__init__()` method in the python standard library does not call
  `super().__init__()`. Because of this oversight, if you don't inherit from `MyPlugin` first, the
  `MyPlugin.__init__()` method will never be called.
- You probably want your plugin to be able to override methods from `cmd2.Cmd`.


### Add commands

### Override methods

Your plugin can override core `cmd2` methods, changing their behavior.

### Decorator

Your plugin can provide a decorator which users of your plugin can use to wrap
functionality around their `cmd2` commands.

## Classes and Functions

Your plugin can also provide classes and functions which can be used by
developers of `cmd2` based applications. Describe these classes and functions in
your documentation so users of your plugin will know what's available.



These hooks get called for every command. If you want to run your plugin code
for only some commands, you can write a bunch of logic into these hook methods,
or you can create a decorator which users of your plugin can selectively apply
to methods.

## Application Lifecycle

The typical way of starting a cmd2 application is as follows:

```python
    import cmd2
    class App(cmd2.Cmd):
        # customized attributes and methods here

    if __name__ == '__main__':
        app = App()
        app.cmdloop()
```

Your plugin can register methods to be called at the beginning or end
of the command loop. These methods do not take any parameters, and return
values are ignored. The best way to utilize these capabilities is to have
a mixin class containing the methods you want called, and then register
those hook methods in the mixin initialization:

```python
class MyPlugin:
    """A mixin class for my plugin"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_preloop_hook(self.preloop_hook)
        self.register_postloop_hook(self.postloop_hook)

    def preloop_hook(self) -> None:
        self.poutput("preloop hook")

    def postloop_hook(self) -> None:
        self.poutput("postloop hook")
```


## Command Processing Loop

You can run code at any of the following points in the command processing lifecycle:

- postparsing_precmd - after the line has been parsed, but before the command is run
- precmd - output has been redirected, timing has started, but command has not been run
- postcmd - command has been run, but output is still redirected, and timing is still Running
- postparsing_postcmd

You should not override these methods to inject your plugin functionality. It's
possible that the user of your plugin might also want to override these methods,
and if they forget to call `super()`, then your plugin functionality will never
get run. In addition, it's complicated if there are multiple plugins trying to
hook the same methods.

To avoid these potential issues, `cmd2` allows a plugin to register one or more
functions for each point in the command processing lifecycle.

register_preloop
register_postloop

Here's the sequence of events (from `cmd2.Cmd.onecmd_plus_hooks`)

1. accept user input
2. call functions registered with `register_preparsing_hook()`
2. parse user input into Statement object
3. call functions registered with `register_postparsing_hook()`
4. call `postparsing_precmd()` - for backwards compatibility deprecated
5. redirect output, if user asked for it and it's allowed
6. start command timer
7. call functions registered with `register_precmd_hook()`
8. call `precmd()` - for backwards compatibility
9. add item to history
10. call `do_command` method
11. call functions registered with `register_postcmd_hook()`
12. call `postcmd()` - for backwards compatibility
13. stop timer
14. stop redirecting output, if it was redirected
15. call functions registered with `register_cmdcompleted_hook()`
16. call `postparsing_postcmd()` - for backwards compatibility - deprecated

TODO - figure out where stop's are

register_preloop_hook
register_postloop_hook

register_preparsing_hook
register_postparsing_hook
register_precmd_hook
register_postcmd_hook
register_cmdcompleted_hook





## License

Cmd2 uses the very liberal MIT license. We invite plugin authors to
consider doing the same.

## Testing

Make sure you test on all versions of python supported by `cmd2`, and on
all supported platforms. `cmd2` uses a three tiered testing strategy to
accomplish this objective.

- [pytest](https://pytest.org) runs the unit tests
- [tox](https://tox.readthedocs.io/) runs the unit tests on multiple versions
  of python
- [AppVeyor](https://www.appveyor.com/) and [TravisCI](https://travis-ci.com)
  run the tests on the various supported platforms

This plugin template is all set up to use the same strategy.

### Running unit tests

Run `pytest` from the top level directory of your plugin to run all the
unit tests.

### Use tox to run unit tests in multiple versions of python

The included `tox.ini` is setup to run the unit tests in python 3.4, 3.5,
and 3.6. In order for `tox` to work, you need to have different versions of
python executables available in your path.
[pyenv](https://github.com/pyenv/pyenv) is one method of doing this easily.
Once `pyenv` is installed, use it to install multiple versions of python:

```
$ pyenv install 3.4.8
$ pyenv install 3.5.5
$ pyenv install 3.6.5
$ pyenv local 3.6.5 3.5.5 3.4.8
```

This will create a `.python-version` file and instruct the `pyenv` shims
to make `python3.6`, `python3.5`, and `python3.4` launch the appropriate
versions of python.

Once these executables are configured, invoking `tox` will create a
virtual environment for each version of python, install the prerequisite
packages, and run your unit tests.


### Run unit tests on multiple platforms

AppVeyor and TravisCI offer free plans for open source projects.


## Examples

Include an example or two in the `examples` directory that shows a
developer how your plugin works, and how to utilize it from within their
application.


## Distribution and Packaging

When creating your `setup.py` file, keep the following in mind:

- use the keywords `cmd2 plugin` to make it easier for people to find your plugin
- since `cmd2` uses semantic versioning, you should use something like `install_requires=['cmd2 >= 0.9.3, <=2']` to make sure that your plugin doesn't try and run with a future version of `cmd2` with which it may not be compatible


