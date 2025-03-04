import os 
def check_path_detailes(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    print(f"The path '{path}' exists.")
    
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    print(f"Dicrectory: {directory}")
    print(f"Filename: {filename}")
    