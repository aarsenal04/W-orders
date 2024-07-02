import logging
import os
from datetime import datetime

current_dir = os.getcwd()
current_time = datetime.now().strftime('%Y-%m-%d %H_%M_%S')
log_filename = f'{current_dir}/Logs/Log_files/log_messages_{current_time}.log'

'''

Logging allows sending messages (including exceptions) to log files rather than printing them to the console.

Logging levels from least to most important:

- DEBUG: Detailed information, typically of interest only when diagnosing problems. (Level 10)
- INFO: Confirmation that things are working as expected. (Level 20)
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected. (Level 30)
- ERROR: Due to a more serious problem, the software has not been able to perform some function. (Level 40)
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running. (Level 50)

Examples:

- logging.debug("Detailed debug message")
- logging.info("Informational message")
- logging.warning("Warning message: Potential issue ahead")
- logging.error("Error message: Something went wrong")
- logging.critical("Critical error: System unable to proceed")

'''

# Set logging configuration to display messages with severity level 'DEBUG' or higher
logging.basicConfig(level=10,
                    format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
                    filename=log_filename,
                    filemode='a')

# test
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''