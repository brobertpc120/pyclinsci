# Copyright 2024 pyclinsci authors. See license.md file for details.
"""Main package of pyclinsci."""

# Import package methods
from pyclinsci._settings import (
    MODULE_PATH,
    __version__,
    __version_info__,
    config_logging,
)

# Declare package methods
__all__ = [
    "MODULE_PATH",
    "__version__",
    "__version_info__",
    "config_logging",
]
