#!/usr/bin/env python
# -*- coding:Utf-8 -*-


#from python
import os
import re

project_path = os.path.realpath(os.path.dirname(__file__))

# from project
try:
    import settings
except ImportError:  # Is it really useful ?
    try:
        # Let's supppose the script is in PROJECT/django-sphinx-autodoc/
        import sys
        project_path = os.path.realpath(os.path.join(project_path, '..'))
        # Add project path to PYTHONPATH
        sys.path.insert(0, project_path)
        import settings  # NOQA
    except ImportError:
        raise ImportError("The script should be run from the project root")


class Modules(object):
    """
    modules.rst file to store all the apps automodules
    """

    def __init__(self):
        self.l_file = []

    def write(self):
        """Write the created list in the new file"""
        f = open("%s.rst" % self.fname, "w+")
        f.writelines(self.l_file)
        f.close()

    def set_name(self, l):
        """
        Verify that a "modules" file is not in the toctree, otherwise rename
        it in "auto_modules"
        """
        re_m = re.compile("modules")
        self.fname = re_m.findall("".join(l)) and "auto_modules" or "modules"
        # Now that we know the title, append it at the beginning of the file
        self.set_title()

    def add_lf(self, l):
        """Append line feed \n to all elements of the given list"""
        return ["%s\n" % line for line in l]

    def set_title(self):
        """ Add title to modules.rst, mandatory """
        symbol_line = "=" * len(self.fname)
        l_title = self.add_lf([symbol_line, self.fname, symbol_line, "", ""])
        l_title.extend(self.l_file)
        self.l_file = l_title

    def add_app(self, app):
        """template of application autodoc"""
        if not app.is_internal:
            return
        # Write the name of the application
        template = self.add_lf([app.name, "=" * len(app.name), ""])

        # Write an automodule for each of its modules
        for module in app.modules:
            template += self.add_lf([
                # title of the module
                module, "-" * len(module), "",
                # automodule
                ".. automodule:: %s.%s" % (app.name, module),
                "    :members:",
                "    :undoc-members:",
                "    :show-inheritance:", ""
            ])
        self.l_file.extend(template)


class App(object):
    """Application with its name and the list of python files it contains"""

    def __init__(self, name):
        self.name = name
        self.is_internal = True
        self.modules = self.get_modules()

    def get_modules(self):
        """Scan the repository for any python files"""
        try:
            excludes = ["__init__.py"]
            return [name.split(".py")[0] for name in os.listdir(self.name)
                       if name.endswith(".py") and name not in excludes]
        except OSError:
            # Currently we just add internal apps (located within the project)
            self.is_internal = False
            pass 

try:
    # Get the list of applications from the settings
    from settings import INSTALLED_APPS as l_apps

    # Create a file for new modules
    f_modules = Modules()
    # Write all the apps autodoc in the newly created file
    [f_modules.add_app(App(name)) for name in l_apps]

    # Go to the doc directory and open the index
    path = os.path.join(project_path, "doc")
    os.chdir(path)
    f_index = open("index.rst", "r")
    l_index = f_index.readlines()
    # Set the file name for modules
    f_modules.set_name(l_index)
    f_index.close()

    # Write the modules file
    f_modules.write()

    # append the new file name to the index.rst
    for i, line in enumerate(l_index):
        if ":maxdepth: 2" in line:
            l_index.insert(i + 2, "    %s\n" % f_modules.fname)
            break
    f_index = open("index.rst", "w")
    f_index.writelines(l_index)
    f_index.close()
except AttributeError, e:
    print e
