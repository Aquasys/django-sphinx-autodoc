#!/usr/bin/env python

import os
from setuptools import setup, find_packages

setup(
    name='django-sphinx-autodoc',
    version="0.1",
    author='Adrien Lemaire',
    author_email='lemaire.adrien@gmail.com',
    description='Autodoc all apps from a project to Sphinx',
    long_description=open(os.path.join(os.path.dirname(__file__),
                           'README.rst')).read(),
    url='http://github.com/Fandekasp/django-sphinx-autodoc',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python",
    ],
)
