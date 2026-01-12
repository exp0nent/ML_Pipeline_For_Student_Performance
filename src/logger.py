import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
                        
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",   
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")

"""A logger in Python is a core component of the built-in logging module, which provides a flexible framework for tracking events 
that happen when software runs. It allows developers to record diagnostic information, errors, and general status messages systematically,
which is crucial for debugging, monitoring application performance, and analyzing issues in production environments.  
(https://blog.sentry.io/logging-in-python-a-developers-guide/)"""
