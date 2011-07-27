#!/usr/bin/env python
# -*- coding:Utf-8 -*-


#from python
import os
import re

HERE = os.path.realpath(os.path.dirname(__file__))

# from project
try:
    # Get the list of applications from the settings
    import settings
    from django.core.management import setup_environ
    setup_environ(settings)  # some apps will fail to load without some
                             # specific settings
except ImportError:
    raise ImportError("The script should be run from the project root")


class Modules(object):
    """
    auto_modules.rst file to store all the apps automodules
    """

    def __init__(self):
        self.internal_apps = []
        self.external_apps = []
        self.fname = settings.DS_FILENAME

    def write(self):
        """Write the created list in the new file"""
        f = open("%s.rst" % self.fname, "w+")
        title = "Internal Applications"
        symbol_line = "=" * len(name)
        l_file = self.add_lf([symbol_line, title, symbol_line, "", ""])
        l_file.extend(self.internal_apps)
        title = "External Applications"
        external_title = self.add_lf([symbol_line, title, symbol_line, "", ""])
        l_file.extend(external_title)
        l_file.extend(self.external_apps)
        f.writelines(l_file)
        f.close()

    def add_to_toctree(self, toctree):
        """
        Verify that a "auto_modules" file is in the toctree, and append it
        otherwise
        """
        re_m = re.compile(settings.DS_FILENAME)
        self.in_index = re_m.findall("".join(toctree)) and True or False
        # Now that we know the title, append it at the beginning of the file

    def add_lf(self, l):
        """Append line feed \n to all elements of the given list"""
        return ["%s\n" % line for line in l]

    def add_app(self, app):
        """template of application autodoc"""

        if not app.path:
            # App couldn't be documented
            #template += ".. error:: This app couldn't be documented\n\n"
# TODO Most themes doesn't style error, need to custom it
            template = ".. warning:: '%s' couldn't be documented\n\n" % app.name  # NOQA
        else:
            # Write the name of the application
            template = self.add_lf([app.name, "=" * len(app.name), ""])

            if app.has_description():
                # Description of the application if it exists
                template += ".. automodule:: %s\n\n" % app.name
            if not app.modules:
                template += ".. warning:: This app has no documentation\n\n"

            # Write an automodule for each of its modules
            for module in app.modules:
                template += self.add_lf([
                    # title of the module
                    module, "-" * len(module), "",
                    # automodule
                    ".. automodule:: %s.%s" % (app.name, module),
                    "    :deprecated:",
                    "    :members:",
                    "    :undoc-members:",
                    "    :show-inheritance:", "",
                ])
        if app.is_internal:
            self.internal_apps.extend(template)
        else:
            self.external_apps.extend(template)


class App(object):
    """Application with its name and the list of python files it contains"""

    def __init__(self, name):
        self.name = name
        self.is_internal = self.name in os.listdir(HERE)
        self.path = self.get_path()
        self.modules = self.get_modules()

    def get_path(self):
        """return absolute path for this application"""
        try:
            path = __import__(self.name).__path__[0]
            splitedName = self.name.split(".")
            if len(splitedName) > 1:
                path = os.path.join(path, *splitedName[1:])
            return path
        except ImportError:
            print "The application %s couldn't be autodocumented" % self.name
            return False

    def get_modules(self):
        """Scan the repository for any python files"""
        if not self.path:
            return []
        # Move inside the application
        os.chdir(self.path)

        modules = [f.split(".py")[0] for f in os.listdir(".") if f not
                   in settings.DS_EXCLUDED_MODULES and f.endswith(".py")]
        # Remove all irrelevant modules. A module is relevant if he
        # contains a function or class
        not_relevant = []
        for module in modules:
            f_module = open("%s.py" % module, "r")
            content = f_module.read()
            f_module.close()
            keywords = ["def", "class"]
            relevant = sum([value in content for value in keywords])
            if not relevant:
                not_relevant.append(module)
                print "%s.%s not relevant, removed" % (self.name, module)
        [modules.remove(module) for module in not_relevant]
        return modules


    def has_description(self):
        """Get the application docstring from __init__.py if it exists"""
        f_init = open("%s/__init__.py" % self.path, "r")
        content = f_init.read()
        if '"""' in content or "'''" in content:
            return True
        return False


if __name__ == '__main__':
    # Define some variables
    settings.DS_ROOT = getattr(settings, "DS_ROOT", os.path.join(HERE, "doc"))
    settings.DS_MASTER_DOC = getattr(settings, "DS_MASTER_DOC", "index.rst")
    settings.DS_FILENAME = getattr(settings, "DS_FILENAME", "auto_modules")
    settings.DS_EXCLUDED_APPS = getattr(settings, "DS_EXCLUDED_APPS", [])
    settings.DS_EXCLUDED_MODULES = getattr(settings, "DS_EXCLUDED_MODULES",
        ["__init__.py", ])

    # Create a file for new modules
    f_modules = Modules()
    # Write all the apps autodoc in the newly created file
    l_apps = set(settings.INSTALLED_APPS) - set(settings.DS_EXCLUDED_APPS)
    [f_modules.add_app(App(name)) for name in l_apps]

    # Go to the doc directory and open the index
    os.chdir(settings.DS_ROOT)
    try:
        f_index = open(settings.DS_MASTER_DOC, "r")
        l_index = f_index.readlines()
        # Set the file name for modules
        f_modules.add_to_toctree(l_index)
        f_index.close()
    except IOError:
        raise IOError("No file %s/%s exists, please fix it" %
             (settings.DS_ROOT, settings.DS_MASTER_DOC))

    # Write the modules file
    f_modules.write()

    # append the new file name to the index.rst
    if not f_modules.in_index:
        for i, line in enumerate(l_index):
            if ":maxdepth: 2" in line:
                l_index.insert(i + 2, "    %s\n" % f_modules.fname)
                break
    f_index = open(settings.DS_MASTER_DOC, "w")
    f_index.writelines(l_index)
    f_index.close()
