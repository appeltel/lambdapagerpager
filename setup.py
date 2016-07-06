#!/usr/bin/env python

from distutils.core import setup

setup(
    name='LambdaPagerPager',
    version='0.0.0',
    description='Flask app to page you if your lambdapager is down',
    author='Eric Appelt',
    author_email='eric.appelt@gmail.com',
    url='https://github.com/appeltel/lambdapagerpager',
    packages=['lambdapagerpager'],
    install_requires = ['Flask', 'twilio', 'bcrypt', 'redis']
)
