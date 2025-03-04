def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src, open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(src.read())  
        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully!")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"Error: {e}")

copy_file("source.txt", "destination.txt")  
