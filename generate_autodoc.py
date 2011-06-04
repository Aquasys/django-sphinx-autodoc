#!/usr/bin/env python
# -*- coding:Utf-8 -*-


#from python
import os
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


try:
    path = os.path.join(project_path, "doc")
    # Go to the doc directory and open the index
    os.chdir(path)
    index = open("index.rst", "r")
    l_index = index.readlines()
    index.close()
    for i, line in enumerate(l_index):
        if ":maxdepth: 2" in line:
            l_index.insert(i + 2, "    bob\n")
            break
    index = open("index.rst", "w")
    index.writelines(l_index)
    index.close()
except AttributeError, e:
    print e
