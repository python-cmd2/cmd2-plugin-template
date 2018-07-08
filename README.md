# cmd2 Plugin Template

## Table of Contents

- [Using this template](#using-this-template)
- [Naming](#naming)
- [Adding functionality](#adding-functionality)
- [Testing](#testing)
- [Examples](#examples)
- [Packaging and Distribution](#packaging-and-distribution)
- [License](#license)


## Using this template

This template assumes you are creating a new cmd2 plugin called `myplugin`. Your
plugin will have a different name. You will need to rename some of the files and
directories in this template. Don't forget to modify the imports and `setup.py`.

You'll probably also want to rewrite the README :)


## Naming

You should prefix the name of your project with `cmd2-`. Within that project,
you should have a package with a prefix of `cmd2_`.


## Adding functionality

There are many ways to add functionality to `cmd2` using a plugin. Most plugins
will be implemented as a mixin. A mixin is a class that encapsulates and injects
code into another class. Developers who use a plugin in their `cmd2` project,
will inject the plugin's code into their subclass of `cmd2.Cmd`.


### Mixin and Initialization

The following short example shows how to mix in a plugin and how the plugin
gets initialized.

Here's the plugin:

```python
class MyPlugin:
    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2.Cmd initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2.Cmd initializes
```

and an example app which uses the plugin:

```python
import cmd2
import cmd2_myplugin

class Example(cmd2_myplugin.MyPlugin, cmd2.Cmd):
    """An class to show how to use a plugin"""
    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2.Cmd or
        # any plugins initialize
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2.Cmd and
        # all plugins have initialized
```

Note how the plugin must be inherited (or mixed in) before `cmd2.Cmd`. This is
required for two reasons:

- As of python 3.6.5, the `cmd.Cmd.__init__()` method in the python standard library does not call
  `super().__init__()`. Because of this oversight, if you don't inherit from `MyPlugin` first, the
  `MyPlugin.__init__()` method will never be called.
- You may want your plugin to be able to override methods from `cmd2.Cmd`.
  If you mixin the plugin after `cmd2.Cmd`, the python method resolution order
  will call `cmd2.Cmd` methods before it calls those in your plugin.


### Add commands

Your plugin can add user visable commands. You do it the same way in a plugin
that you would in a `cmd2.Cmd` app:

```python
class MyPlugin:

    def do_say(self, statement):
        """Simple say command"""
        self.poutput(statement)
```

You have all the same capabilities within the plugin that you do inside a
`cmd2.Cmd` app, including argument parsing via decorators and custom help
methods.

### Add (or hide) settings

A plugin may add user controllable settings to the application. Here's an
example:

```python
class MyPlugin:
    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2.Cmd initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2.Cmd initializes
        self.mysetting = 'somevalue'
        self.settable.update({'mysetting': 'short help message for mysetting'})
```

You can also hide settings from the user by removing them from `self.settable`.

### Decorators

Your plugin can provide a decorator which users of your plugin can use to wrap
functionality around their own commands.

### Override methods

Your plugin can override core `cmd2.Cmd` methods, changing their behavior.
This approach should be used sparingly, because it is very brittle. If a
developer chooses to use multiple plugins in their application, and several of
the plugins override the same method, only the first plugin to be mixed in
will have the overridden method called.

Hooks are a much better approach.

### Hooks

Plugins can register hooks, which are called by `cmd2.Cmd` during various points
in the application and command processing lifecycle. Plugins should not override
any of the deprecated hook methods, instead they should register their hooks as
[described](https://cmd2.readthedocs.io/en/latest/hooks.html) in the cmd2
documentation.

Here's a simple example:

```python
class MyPlugin:

    def __init__(self, *args, **kwargs):
        # code placed here runs before cmd2 initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2 initializes
        # this is where you register any hook functions
        self.register_postparsing_hook(self.postparsing_hook)

    def postparsing_hook(self, data: cmd2.plugin.PostparsingData) -> cmd2.plugin.PostparsingData:
        """Method to be called after parsing user input, but before running the command"""
        self.poutput('in postparsing_hook')
        return data
```

Registration allows multiple plugins (or even the application itself) to each inject code
to be called during the application or command processing lifecycle.

See the [cmd2 hook documentation](https://cmd2.readthedocs.io/en/latest/hooks.html)
for full details of the application and command lifecycle, including all
available hooks and the ways hooks can influence the lifecycle.


### Classes and Functions

Your plugin can also provide classes and functions which can be used by
developers of cmd2 based applications. Describe these classes and functions in
your documentation so users of your plugin will know what's available.


## Testing

Make sure you test on all versions of python supported by cmd2, and on
all supported platforms. cmd2 uses a three tiered testing strategy to
accomplish this objective.

- [pytest](https://pytest.org) runs the unit tests
- [tox](https://tox.readthedocs.io/) runs the unit tests on multiple versions
  of python
- [AppVeyor](https://www.appveyor.com/) and [TravisCI](https://travis-ci.com)
  run the tests on the various supported platforms

This plugin template is set up to use the same strategy.


### Running unit tests

Run `pytest` from the top level directory of your plugin to run all the
unit tests.


### Use tox to run unit tests in multiple versions of python

The included `tox.ini` is setup to run the unit tests in python 3.4, 3.5, 3.6,
and 3.7. In order for `tox` to work, you need to have different versions of
python executables available in your path.
[pyenv](https://github.com/pyenv/pyenv) is one method of doing this easily. Once
`pyenv` is installed, use it to install multiple versions of python:

```
$ pyenv install 3.4.8
$ pyenv install 3.5.5
$ pyenv install 3.6.5
$ pyenv install 3.7.0
$ pyenv local 3.7.0 3.6.5 3.5.5 3.4.8
```

This will create a `.python-version` file and instruct the `pyenv` shims to make
`python3.7`, `python3.6`, `python3.5`, and `python3.4` launch the appropriate
versions of python.

Once these executables are configured, invoking `tox` will create a virtual
environment for each version of python, install the prerequisite packages, and
run your unit tests.


### Run unit tests on multiple platforms

AppVeyor and TravisCI offer free plans for open source projects.


## Examples

Include an example or two in the `examples` directory which demonstrate how your
plugin works. This will help developers utilize it from within their
application.


## Packaging and Distribution

When creating your `setup.py` file, keep the following in mind:

- use the keywords `cmd2 plugin` to make it easier for people to find your plugin
- since cmd2 uses semantic versioning, you should use something like
  `install_requires=['cmd2 >= 0.9.3, <=2']` to make sure that your plugin
  doesn't try and run with a future version of cmd2 with which it may not be
  compatible


## License

cmd2 [uses the very liberal MIT license](https://github.com/python-cmd2/cmd2/blob/master/LICENSE).
We invite plugin authors to consider doing the same.
