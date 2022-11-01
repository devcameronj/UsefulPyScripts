# ignore this file, it's for development only

import os

check = "python --version"
os.system(check)
upgrade = "python.exe -m pip install --upgrade pip"
start = "pip install -r Custom_Scripts/requirements.txt"
os.system(upgrade)
os.system(start)
