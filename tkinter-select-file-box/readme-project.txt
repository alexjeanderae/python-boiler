===TKINTER SELECT FILE BOX===

This is a simple starter code to have a executable (typically windows) that will call a script after selecting an input file.

User runs the program and selects a file in a typical windows manner. And then the scripts does the rest. The script generates a log file with a timestamp.

===LIBRARIES USED===

Pyinstaller to make the windows executable.

All the others imports do not require pip and are vanilla.
Tkinter for the GUI - some part of it as the lib does much more.
Datetime and logging. 
Script was originally written with Python 3.9.6

===TO REMEMBER===
1- Weird import syntax. I had an error "ModuleNotFoundError: No module named" and the file name I try to import
from  .tkinter_dialog import open_file_with_inputs --> added a . to make a relative import! It fixed it.
2- I encountered further import/packaging issues in the use of pysinstaller. And generally the code could follow DRY better. Good reads:
https://iq-inc.com/importerror-attempted-relative-import/
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
https://stackoverflow.com/questions/60988011/pyinstaller-importerror-on-own-module

3-Make a quick icon to get going. I used canva, saved a png, then used another app to get an .ico file. The selected size is 48x48 px which is quite small.

4-Pyinstaller as a one liner in the CLI for something quick. The dist file it creates will have a .exe file. You can rename 
the executable after it is output if you want.
pyinstaller.exe --onefile -w --icon=xyz.ico name_of_entry_file.py
The -w or --windowed flag is to avoid a blackbox at the back that is some kind of a command prompt looking thing :D. Also using .pyw extensions instead of .py seem also to solve this. 
There is a great timesaver resource on pyinstaller official doc - https://pyinstaller.org/en/stable/when-things-go-wrong.html


===TO IMPROVE===
#TODO: here is the main list
- Had some issues with CLI on certain use case (default values with flags) I would like to revisit the solution of. I am pretty sure there is more readable way -pythonic!- way to deal with these. See private repos and decide what to handle here on public.
- Message to open prints where?
- Call a test when tkinter opens the file to make sure that the contents are as needed?
- Do we want to open multiple files? https://stackoverflow.com/questions/16790328/open-multiple-filenames-in-tkinter-and-add-the-filesnames-to-a-list
- Do some visual improvements to the GUI - check this series https://www.youtube.com/watch?v=QWqxRchawZY
