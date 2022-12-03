===TKINTER SELECT FILE BOX===

This is a simple starter code to have a executable (typically windows) that will call a script after selecting an input file.

User runs the program and selects a file in a typical windows manner. And then the scripts does the rest. The script generates a log file with a timestamp.

===LIBRARIES USED===

Pyinstaller to make the windows executable.

All the others imports do not require pip and are vanilla.
Tkinter for the GUI - some part of it as the lib does much more.
Datetime and logging. 
Script was originally written with Python 3.9.6

Current command to run pyinstaller
pyinstaller.exe --onefile -w --hidden-import utils.logging_utils --hidden-import utils.tkinter_dialog--icon=select-file-box.ico py_installer_entry.py

===LESSONS LEARNT===
1-Confirmed - Need an init file in all folder containing .py files and their respective subfolders. From the official doc: "The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later." That did not solve the import module bug I had with pysintaller.
"if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered."
__all__ = ["file1", "file4", "file5"]
Good read: https://docs.python.org/3/tutorial/modules.html#packages


===TO REMEMBER===
1- Weird import syntax. I had an error "ModuleNotFoundError: No module named" and the file name I try to import
from  .tkinter_dialog import open_file_with_inputs --> added a . to make a relative import! It fixed it. But then it created other issues. Generally it seems absolute -not relative- imports is the most robust solution in Python. Absolute import is typically "from subfolder.filename import functionname". You can then call functionname() directly in the code
2- I encountered further import/packaging issues in the use of pysinstaller. And generally the code could follow DRY better. Good reads:
https://iq-inc.com/importerror-attempted-relative-import/
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
https://stackoverflow.com/questions/60988011/pyinstaller-importerror-on-own-module

3-Make a quick icon to get going. I used canva, saved a png, then used another app to get an .ico file. The selected size is 48x48 px which is quite small.

4-Pyinstaller as a one liner in the CLI for something quick. The dist file it creates will have a .exe file. You can rename 
the executable after it is output if you want.
pyinstaller.exe --onefile -w --icon=xyz.ico name_of_entry_file.py
The -w or --windowed flag is to avoid a blackbox at the back. Might be wanted though as it prints console. 

5- There is a great timesaver resource on pyinstaller official doc - https://pyinstaller.org/en/stable/when-things-go-wrong.html


===FURTHER POLISH - POSSIBLE IMPROVEMENTS===
1- I could not get the modules to load properly if in sub folders. I tried 5 different solutions on SO, read docs. Was not working for me on this code base. Not a drama as I can flatten the folder structure to just one. But in the future, I might want to revisit this.
2- Comment/Document the module imports repairs
3- Have a yaml file that runs all commands
4- Comment/Document the addition of the yaml file
5- Add testing layer
6- Comment/Document the testing addition
7- Add Docstring and document the experience
8 - Review the document of the whole thing using Docstring 
9- Finalize the core
10- Start tackling the improvements on rainy days.


===TO IMPROVE===
#TODO: here is the main list
- Had some issues with CLI on certain use case (default values with flags) I would like to revisit the solution of. I am pretty sure there is more readable way -pythonic!- way to deal with these. See private repos and decide what to handle here on public.
- Message to open prints where?
- Call a test when tkinter opens the file to make sure that the contents are as needed?
- Do we want to open multiple files? https://stackoverflow.com/questions/16790328/open-multiple-filenames-in-tkinter-and-add-the-filesnames-to-a-list
- Do some visual improvements to the GUI - check this series https://www.youtube.com/watch?v=QWqxRchawZY
- Improve the init file?
- Do the modular approach as in the hitchiker guide to python