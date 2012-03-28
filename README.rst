=====================
Django-Sphinx-autodoc
=====================


.. note::

    Being overwhelmed by work, I won’t upgrade this package if nobody asks for
    it. If you’re capable, please fork and pull request to help me, thanks in
    advance !


Django is very nice in that way you can reuse a lot of applications in your
projects. It means for big projects that you'll get a long list of applications
in your settings.INSTALLED_APP.

If you're using Django with Sphinx and want to autodoc all these apps in a wink
of an eye, then this app is for you.

A good combinaison for documenting your project would be:
 - **sphinx**
 - **django-sphinx-autodoc** to generate the doc from your applications
 - **django-sphinxdoc** to integrate the sphinx doc in your website


How it works
------------

Copy the generate_autodoc.py file in your project directory, then execute it.

It will scrape all your .py files in each application listed by INSTALLED_APP,
then add automodules in your DS_ROOT/modules.rst.

You will then see your applications grouped in 2 different categories:

- **internal application** is an application located in your project directory
- **external application** is an app which is somewhere in your pythonpath
  (preferably in your virtualenv)

Good Practices
--------------

Add a docstring in your application's __init__.py file to describe it.
django-sphinx-autodoc will automatically scrape it for you.


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

- Write tests
- improve the not_relevant stuff to auto exclude a file without class or def
- Django command extension to update the autodoc
