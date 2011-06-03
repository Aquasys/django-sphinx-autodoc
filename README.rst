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
