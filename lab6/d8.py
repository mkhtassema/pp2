import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    if not os.access(file_path, os.W_OK): 
        print("Error: No permission to delete the file.")
        return

    try:
        os.remove(file_path)  
        print(f"File '{file_path}' deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

file_path = "test.txt"  
delete_file(file_path)
