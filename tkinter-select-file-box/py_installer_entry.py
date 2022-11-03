#py_installer_entry.py

from  tkinter_dialog import open_file_with_inputs
from logging_utils import create_log_txt_file

def app_entry(): 
    create_log_txt_file()
    open_file_with_inputs()


app_entry()