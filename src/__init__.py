import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(modeule)s: %(message)s]"

log_dir = 'logs'
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # initializes log file and prints log in file
        logging.streamHandler(sys.stdout) # print log in terminal
    ]
)


logger = logging.getLogger("bookMogger")