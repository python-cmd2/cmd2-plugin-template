#
# coding=utf-8

import os
import setuptools

#
# get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION='0.1.0'

setuptools.setup(
    name='cmd2-myplugin',
    version=VERSION,
    description='A template used to build plugins for cmd2',
    long_description=long_description,
    keywords='cmd2 plugin',

    author='Kotfu',
    author_email='kotfu@kotfu.net',
    url='https://github.com/python-cmd2/cmd2-plugin-template',
    license='MIT',

    packages=['cmd2_myplugin'],

    python_requires='>=3.4',
    install_requires=['cmd2 >= 0.9.3, <=2'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # dependencies for development and testing
    # $ pip install -e .[dev]
    extras_require={
        'dev': ['pytest']
    },
)
