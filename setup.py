#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import connected_accounts

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = connected_accounts.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='django-connected',
    version=version,
    description="""Connect your Django powered sites to social networks and other online services.""",
    long_description=readme,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/django-connected',
    packages=[
        'connected_accounts',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'jsonfield',
        'requests>=1.0',
        'requests_oauthlib>=0.3.0',
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-connected, social auth, oauth, oauth2, facebook, twitter, google',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
