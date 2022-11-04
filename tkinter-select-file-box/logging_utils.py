# logging_utils.py

import logging
from time_stamp_util import generate_short_timestamp


""" This script creates a logging text file to save the output of other logging operations
It calls another script that generates a timestamp and extension based filename for the log"""

def create_log_txt_file():
    time_in_string = generate_short_timestamp()
    generated_name = "log_" + time_in_string +".txt"
    logging.basicConfig(filename=generated_name, level=logging.DEBUG)  #lowest level of logged message at "debug" level
    logging.debug("file created " + generated_name) 


if __name__ == '__main__':
        print("running the invoked script standalone")
        create_log_txt_file()