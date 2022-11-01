# I got annoyed starting the webserver manually and forgetting the command
# ignore this file, it's for development only

import os

check = "python --version"
os.system(check)
start = "python -m http.server 8000"
os.system(start)
