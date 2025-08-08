import logging
from datetime import date
import config
"""
Module for logging configuration and setup.
This module configures the logging settings for the application, including the log file name,
log level, and log format. It also provides a function to set up the logging system.
"""
# Set up logging configuration

def set_log() -> None:
    """
    Basic logging configuration. Log file name starts with the current date for tracking.
    """
    filename = f"{config.log_directory}{str(date.today())}-logfile.log"
    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s %(levelname)s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        filename = filename
    )
    lines = 0
    with open(filename, "r") as logfile:
        lines = len(logfile.readlines())

    if lines > 0:
        with open(filename, "a") as logfile:
            logfile.write("\n")  # Separates blocks of log entries