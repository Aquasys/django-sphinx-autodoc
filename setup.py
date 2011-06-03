#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-sphinx-autodoc',
    version="0.0",
    author='Adrien Lemaire',
    author_email='lemaire.adrien@gmail.com',
    description='Autodoc all apps from a project to Sphinx',
    url='http://github.com/Fandekasp/django-sphinx-autodoc',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
