# Copyright 2024 pyclinsci authors. See license.md file for details.

# Import objects
from importlib.metadata import version
from importlib.util import find_spec
from pathlib import Path
from re import Match, match
from sys import modules, stderr
from typing import cast

from loguru import logger

# Set MODULE_NAME constant
MODULE_NAME = modules[__name__].__name__.split(".")[0]
"""Name of the module"""

# Set module constants
MODULE_PATH: str = Path(find_spec(MODULE_NAME).origin).parent
"""Absolute path of the module."""

# Extract version information
__version__: str = version(MODULE_NAME)
"""Version of the module."""

# Build version information string
result = cast(Match[str], match(r"(\d+\.\d+\.\d+).*", __version__))
__version_info__: tuple[str] = tuple(result.group(1).split("."))
"""Version information of the module"""

def config_logging(console: str = "NONE", file: str = "NONE") -> None:
    """Configure logging settings for the application.

    This function resets the logging handlers and configures logging to
    a rotating file named 'loguru.log' with a rotation interval of 5
    seconds. It also configures logging to the standard error stream
    (stderr) for console output.

    Returns
    -------
        None

    """
    # Reset logging handlers
    logger.remove()

    # Define logging to a rotating file
    if file != "NONE":
        logger.add(
            "pyclinsci.log",
            rotation="5 seconds",
            level=file,
            format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level}\n{message}\n",
        )
        logger.info("Configured logging in file `pyclinsci.log`.")

    # Define logging to console
    if console != "NONE":
        logger.add(
            stderr,
            level=console,
            format="{time:MMMM D, YYYY > HH:mm:ss!UTC} | {level}\n{message}\n",
        )
        logger.info("Configured logging in console.")
