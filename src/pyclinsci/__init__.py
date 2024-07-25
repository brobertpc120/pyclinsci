# Copyright 2024 pyclinsci authors. See license.md file for details.
"""pyclinsci package -- tools for clinical science projects.

`pyclinsci` is a Python package gathering tools for clinical science
activities. Beyond gathering different tools, the objective of this module is
to provide different method or classes to simplify development of new tools
and accelerate development of these tools.
"""

# Import libraries and objects
from pyclinsci._data import GenericData, GeoData
from pyclinsci._decorators import method_exec_dur
from pyclinsci._files import dialog_select_file_dir
from pyclinsci._settings import (
    MODULE_NAME,
    MODULE_PATH,
    __version__,
    __version_info__,
    config_logging,
)

# Declare package methods
__all__ = [
    "GenericData",
    "GeoData",
    "method_exec_dur",
    "dialog_select_file_dir",
    "MODULE_NAME",
    "MODULE_PATH",
    "__version__",
    "__version_info__",
    "config_logging",
]
