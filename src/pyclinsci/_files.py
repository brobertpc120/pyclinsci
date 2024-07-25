# Copyright 2024 pyclinsci authors. See license.md file for details.

# Import libraries and objects
import os
from pathlib import Path

from loguru import logger
from PyQt6 import QtWidgets


def dialog_select_file_dir(
    dir_path: str = Path.cwd(),
    func    : str = "open",
    opt     : dict[str,str] = frozenset({"*.*": "All files"}),
) -> str:
    """Open a dialog box to select a file or directory using PyQt6 QtWidgets.

    Parameters:
        dir_path (str, default=Path.cwd()): The initial directory path to
            start the dialog box.
        func (str, default="open"): The function to perform - "open" to open a
            file, "save" to save a file, or "dir" to select a directory.
        opt (dict[str,str], default={"*.*": "All files"}): Optional parameter
            to specify file types to filter.

    Returns:
        str: The selected file path or directory path.

    Raises:
        FileNotFoundError: If the provided directory path is not valid.
        ValueError: If the function parameter 'func' is not valid.

    """
    # Test if path is a directory
    qt_app = QtWidgets.QApplication([])
    if not Path(dir_path).is_dir():
        log_error = "No valid folder path was provided."
        logger.error(log_error)
        raise FileNotFoundError(log_error)

    # Extract file types
    file_types = ";;".join([f"{value} ({key})" for key, value in opt.items()])

    # Control if func parameters are valid
    title = f"{func.capitalize()} a file"
    if func not in ["open", "save", "dir"]:
        log_error  = f"Method cannot handle '{func}' func-parameter."
        logger.error(log_error)
        raise ValueError(log_error)

    # Show dialog box
    if func == "open":
        path = QtWidgets.QFileDialog.getOpenFileName(
            None,
            title,
            str(dir_path),
            file_types,
        )
        path = path[0]

    elif func == "save":
        path = QtWidgets.QFileDialog.getSaveFileName(
            None,
            title,
            str(dir_path),
            file_types,
        )
        path = f"{Path(path[0]).parent}{os.sep}{Path(path[0]).name}"


    elif func == "dir":
        title = "Select a folder"
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            title,
            str(dir_path),
        )

    else:
        err_msg  = f"Method cannot handle '{func}' func-parameter.)"
        raise ValueError(err_msg)

    # Return path
    qt_app.closeAllWindows()
    return path
