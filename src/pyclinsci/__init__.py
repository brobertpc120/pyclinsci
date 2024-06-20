# Copyright 2024 pyclinsci authors. See license.md file for details.
"""Main package of pyclinsci."""

# Import libraries and objects
from pyclinsci._data import GenericData, GeoData
from pyclinsci._decorators import method_exec_dur
from pyclinsci._files import dialog_select_file_dir
from pyclinsci._settings import (
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
    "MODULE_PATH",
    "__version__",
    "__version_info__",
    "config_logging",
]
