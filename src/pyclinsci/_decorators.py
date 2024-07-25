# Import libraries and objects
import time
from collections.abc import Callable
from typing import Any

from loguru import logger


def method_exec_dur(func: Callable[..., Any]) -> Callable[..., Any]:
    """Log the execution duration of a method.

    Parameters:
        func (Callable[..., Any])): The method to be decorated.

    Returns:
        Callable[..., Any]: The wrapped function that logs the execution
            duration of the input method.

    """
    # Define wrapper function
    def wrapper(*args: Any, **kwargs: Any) -> Callable[..., Any]:# noqa: ANN401
        # Log message for entering method
        log_txt = f"Enter {func.__qualname__} method."
        logger.debug(log_txt)

        # Execute function and evaluate execution time
        start_time = time.perf_counter()
        result     = func(*args, **kwargs)
        end_time   = time.perf_counter()

        # Print log message
        log_txt  = f"Method ({func.__qualname__}) was executed in "
        log_txt += f"{end_time - start_time:.2f} sec."
        logger.debug(log_txt)

        # Log message for exiting method
        log_txt = f"Exit {func.__qualname__} method."
        logger.debug(log_txt)

        return result

    return wrapper
