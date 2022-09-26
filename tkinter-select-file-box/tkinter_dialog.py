#tkinter_dialog.py

#using Tk capitalized, then use Tk()
import tkinter as Tk
from tkinter.filedialog import askopenfilename
import logging

def open_file_with_inputs():
        print("Select the file to open with the inputs")
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        logging.info("selected to load " + filename)
        return filename #feeds the file name fpr the rest of the script

#todo: add error handling
# add an error if cannot load the file
# add an error if it is a file of not the right type (typically txt but could extend to others)
