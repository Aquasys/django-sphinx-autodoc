#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.rst') as file:
        long_description = file.read()


setup(
    name='django-sphinx-autodoc',
    version="0.2",
    author='Adrien Lemaire',
    author_email='lemaire.adrien@gmail.com',
    description='Autodoc all apps from a project to Sphinx',
    long_description=long_description,
    url='http://github.com/Fandekasp/django-sphinx-autodoc',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
    ],
)
