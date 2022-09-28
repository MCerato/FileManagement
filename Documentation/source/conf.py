# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# ****************** A éditer pour donner les fichiers pythons sources à documenter ******************

import os
import sys

# from conf.py, go to your Project Directory
# sys.path.insert(0, os.path.abspath("../../.."))


absolutepath = os.path.abspath(__file__)
print(absolutepath)
print("")

sys.path.insert(0, "D:/temp_perso/FileManagement/Sources/Packages/File")
sys.path.insert(0, "D:/temp_perso/FileManagement/Tests")
print(sys.path)
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'FileManagement'
copyright = '2022, M.C.'
author = 'M.C.'

# The full version, including alpha/beta/rc tags
release = '0.0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Turn off prepending module names
add_module_names = False
 
# Sort members by type
autodoc_member_order = 'groupwise'
 
# Document __init__, __repr__, and __str__ methods
def skip(app, what, name, obj, would_skip, options):
    if name in ("__init__", "__repr__", "__str__", "__del__"):
        return False
    return would_skip
 
def setup(app):
    app.connect("autodoc-skip-member", skip)

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']