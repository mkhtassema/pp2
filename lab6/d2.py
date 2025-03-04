import os
def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' doesnt existd ")
        return 
    print(f"The path '{path}' existd ")
    if os.access(path, os.R_OK):
        print("It is readable")
    else:
        print("it is not readable")
    if os.access(path, os.W_OK):
        print("It is writable")
    else:
        print("It is not writable")
    if os.access(path, os.X_OK):
        print("It is executable")
    else:
        print("it is not executable")
path = input()
check_path_access(path)
