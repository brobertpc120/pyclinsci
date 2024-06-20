# Copyright 2024 pyclinsci authors. See license.md file for details.

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

import pyclinsci

sys.path.insert(0, Path("..").resolve())


# -- Project information -----------------------------------------------------

project   = "pyclinsci"
author    = "Contributors of pyclinsci"
version   = ".".join(str(x) for x in pyclinsci.__version_info__[:2])
release   = pyclinsci.__version__


# -- General configuration ---------------------------------------------------

extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = [
    "build",
    "Thumbs.db",
    ".DS_Store",
    "changes/*.rst",
]

numfig              = True
numfig_secnum_depth = 1


# -- Options for Graphviz output ----------------------------------------------

graphviz_output_format = "svg"


# -- Options for HTML output --------------------------------------------------

html_theme           = "furo"
html_show_sourcelink = True


# -- Options for LATEX output -------------------------------------------------

latex_engine        = "pdflatex"
latex_show_pagerefs = True


# -- Options for PYTHON output ------------------------------------------------

python_display_short_literal_types = True


# -- Options for AUTOAPI extension --------------------------------------------

autoapi_dirs                 = ["../../src/pyclinsci"]
autoapi_type                 = "python"
autoapi_file_patterns        = ["*.py"]
autoapi_generate_api_docs    = True
autoapi_keep_files           = False

autoapi_options = [
    "members",                  # display children
    "inherited-members",        # display inherited children
    "undoc-members",            # display objects with no docstring
    "special-members",          # display special objects (__foo__)
    "show-inheritance",         # display a list of base classes
    # "show-inheritance-diagram", # display an inheritance diagram
    "show-module-summary",      # include autosummary directives
    "imported-members",         # display objects from same package or module
]

autoapi_add_toctree_entry    = True
autoapi_python_class_content = "both" # "class"
autoapi_member_order         = "groupwise"
