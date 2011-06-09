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


TODO
----

v1
++

- create settings.py to store some variables
   - SPHINX_INDEX : default to 'index.rst', but you might have changed it
   - MODULES_NAME : name for the modules.rst file if you already use this name
   - EXCLUDED_APPS
   - EXCLUDED_MODULES : default to ['__init__.py'], a module being any python file
- Include external apps (currently only internal apps, located in the project
  root directory)
- Write tests

v2
++

Django command extension to update the autodoc
