# Copyright 2024 pyclinsci authors. See license.md file for details.

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

import pyclinsci
from sphinxawesome_theme.postprocess import Icons

sys.path.insert(0, Path("..").resolve())


# -- Project information -----------------------------------------------------

project   = "pyclinsci"
author    = "Contributors of pyclinsci"
version   = ".".join(str(x) for x in pyclinsci.__version_info__[:2])
release   = pyclinsci.__version__

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

# -- General configuration ---------------------------------------------------

python_display_short_literal_types = True

extensions = [
    "myst_parser",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    # "sphinx.ext.graphviz",
    # "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
]

# -- Options for MYST_PARSER extension ----------------------------------------

myst_heading_anchors = 2
# myst_all_links_external = True

# -- Options for AUTOAPI extension --------------------------------------------

autoapi_dirs                 = ["../../src/pyclinsci"]
autoapi_member_order         = "groupwise"
autoapi_own_page_level       = "class"
autoapi_file_patterns        = ["*.py"]

autoapi_options = [
    "members",                  # display children
    "inherited-members",        # display inherited children
    "undoc-members",            # display objects with no docstring
    "show-inheritance",         # display a list of base classes
    # "show-inheritance-diagram", # display an inheritance diagram
    "show-module-summary",      # include autosummary directives
    "imported-members",         # display objects from same package or module
]

# -- Options for NAPOLEON extension -------------------------------------------

napoleon_google_docstring              = True
napoleon_numpy_docstring               = False

# -- Options for Graphviz output ----------------------------------------------

# graphviz_output_format = "svg"


# -- Options for HTML output --------------------------------------------------

html_theme           = "sphinxawesome_theme"
html_permalinks_icon = Icons.permalinks_icon
html_show_sourcelink = True
html_theme_options = {
}

# -- Options for LATEX output -------------------------------------------------

latex_engine        = "pdflatex"
latex_show_pagerefs = True
