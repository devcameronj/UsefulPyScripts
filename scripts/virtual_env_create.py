# ignore this file, it's for development only

# On Windows, invoke the venv command as follows:
# c:\>c:\Python35\python -m venv c:\path\to\myenv

# Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:
# c:\>python -m venv c:\path\to\myenv

import os

check = "python --version"
os.system(check)
path = input("Full path to environment: ")
create_virtual_env = "python -m venv " + path
os.system(create_virtual_env)
print("**************************************************************************")
print("To start virtual environment, open the terminal and type: 'Scripts/Activate.ps1'")
print("To end a virtual environment, open the terminal while the virtual environment is active and type: 'deactivate'")
print("**************************************************************************")