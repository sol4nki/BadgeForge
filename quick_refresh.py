# this is only for quick development not a dependency when releasing prod
# live reload on saving (getmtime(modif time))

import os, time
import subprocess, sys

file_loc = "./test.py"

process = subprocess.Popen(["python3", file_loc])

while True:
    try:
        last_mtime = os.path.getmtime(file_loc)
        time.sleep(1)
        curr_mtime = os.path.getmtime(file_loc)
        if curr_mtime != last_mtime:
            process.terminate()
            print("changes")
            process = subprocess.Popen(["python3", file_loc])
    except KeyboardInterrupt:
        print("[!!]= Progran exitting =[!!]")
        break