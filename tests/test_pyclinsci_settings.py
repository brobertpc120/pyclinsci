# Copyright 2024 pyclinsci authors. See license.md file for details.
"""Test settings from pyclinsci package."""

# Import modules, functions, constants
from loguru import logger
from pyclinsci import (
    MODULE_PATH,
    __version__,
    __version_info__,
    config_logging,
)

# Initialize logging in this file
config_logging(console="TRACE")

# Access to package description variables
def test_package_version() -> None:
    """Test main constant from pyclinsci package."""
    # Test logging
    logger.trace("A trace message.")
    logger.debug("A debug message.")
    logger.info("An info message.")
    logger.success("A success message.")
    logger.warning("A warning message.")
    logger.error("An error message.")
    logger.critical("A critical message.")

    # Retrieve version info from package and log them
    log_txt  = f"MODULE_PATH: {MODULE_PATH}\n__version__: {__version__}\n"
    log_txt += f"__version_info__: {__version_info__}"
    logger.info(log_txt)
