# Creating a plugin for cmd2

## Using this template

This template assumes you are creating a new cmd2 plugin called `myplugin`. I expect you will want
to give your plugin a different name. You will need to rename some of the files and directories
in this template to your own package name. Don't forget to modify the imports and `setup.py`.

You'll probably also want to rewrite the README :)

## Naming
You should prefix the name of your project with `cmd2-`. Within that project, you should have a package with a prefix of `cmd2_`.

## License

Cmd2 uses the very liberal MIT license. We invite plugin authors to
consider doing the same.

## Tests

Make sure you test on all versions of python supported by `cmd2`, and on
all supported platforms. `cmd2` uses a three tiered testing strategy to
accomplish this objective.

- [pytest](https://pytest.org) runs the unit tests
- [tox](https://tox.readthedocs.io/) runs the unit tests on multiple versions
  of python
- [AppVeyor](https://www.appveyor.com/) and [TravisCI](https://travis-ci.com)
  run the tests on the various supported platforms

AppVeyor and TravisCI offer free plans for open source projects.


## Examples

Include an example or two in the `examples` directory that shows a developer how your plugin
works, and how to utilize it from within their application.


## Distribution and Packaging

When creating your `setup.py` file, keep the following in mind:

- use the keywords `cmd2 plugin` to make it easier for people to find your plugin
- since `cmd2` uses semantic versioning, you should use something like `install_requires=['cmd2 >= 0.9.0, <=2']` to make sure that your plugin doesn't try and run with a future version of `cmd2` with which it may not be compatible


