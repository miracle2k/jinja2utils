#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='jinja2utils',
    url='http://github.com/miracle2k/jinja2utils/',
    license='BSD',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)