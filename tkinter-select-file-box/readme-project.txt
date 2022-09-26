===TKINTER SELECT FILE BOX===

This is a simple starter code to have a executable (typically windows) that will call a script after selecting an input file.

User runs the program and selects a file in a typical windows manner. And then the scripts does the rest. The script generates a log file with a timestamp.

===LIBRARIES USED===

Pyinstaller to make the windows executable.

All the others imports do not require pip and are vanilla.
Tkinter for the GUI - some part of it as the lib does much more.
Datetime and logging. 
Script was written with Python 3.10.

===TO REMEMBER===
1- Weird import syntax. I had an error "ModuleNotFoundError: No module named" and the file name I try to import
from  .tkinter_dialog import open_file_with_inputs --> added a . to make a relative import! It fixed it.


===TO IMPROVE===
#TODO: here is the main list
- Had some issues with CLI on certain use case (default values with flags) I would like to revisit the solution of. I am pretty sure there is more readable way -pythonic!- way to deal with these. See private repos and decide what to handle here on public.
- Message to open prints where?
- Call a test when tkinter opens the file to make sure that the contents are as needed?
- Do we want to open multiple files? https://stackoverflow.com/questions/16790328/open-multiple-filenames-in-tkinter-and-add-the-filesnames-to-a-list
