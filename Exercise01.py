import os
import platform

def find_all_os_functions():
    #print(f"{dir(os)}\n");
    #print(os.uname().sysname)
    print(platform.uname())

find_all_os_functions()
