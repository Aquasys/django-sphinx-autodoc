=====================
Django-Sphinx-autodoc
=====================


Django is awesome in that way you can reuse a lot of applications in your
projects. It means for big projects that you'll get a long list of applications
in your settings.INSTALLED_APP.

If you're using Django with Sphinx and want to autodoc all these apps in a wink
of an eye, then this app is for you.


How it works
------------

It will scrap all your .py files in each application listed by INSTALLED_APP,
then add automodules in your PROJECT/SPHINX_ROOT/modules.rst.

Settings
--------

You can modify some of the settings used by django-sphinx-autodoc:

- **DS_ROOT**: root path for documentation (default to project_dir/doc)
- **DS_MASTER_DOC**: name of your master document (default to "index.rst")
- **DS_FILENAME**: name for the modules (default to "auto_modules.rst")
- **DS_EXCLUDED_APPS**: list of applications to exclude (default to [])
- **DS_EXCLUDED_MODULES**: list of files to exclude (default to ["__init__.py"])


TODO
----

v0.1
++

- Include external apps (currently only internal apps, located in the project
  root directory)
- Write tests

v0.2
++

Django command extension to update the autodoc
