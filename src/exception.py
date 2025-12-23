#The sys library in Python is a built-in module that provides access to system-specific parameters and functions. 
# It's one of the most commonly used standard library modules.
'''Errors and Exceptions Handling things (https://docs.python.org/3/tutorial/errors.html)'''
import sys
import logging
from src.logger import logging

def error_message_detail(error,error_details:sys):
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb = error_details.exc_info()
    error_message = "Error occured in python script name [{0}] line nymber [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

