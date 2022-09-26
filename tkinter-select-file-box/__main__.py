# main.py
from  .tkinter_dialog import open_file_with_inputs
from .logging_utils import create_log_txt_file

def main(): 
    create_log_txt_file()
    open_file_with_inputs()

#TODO: add to the main script

#TODO: spew a logging file that can be opened

if __name__ == '__main__':
        main()