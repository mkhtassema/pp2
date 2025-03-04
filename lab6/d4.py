def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print("Error: File not found.")
        return None

filename = "example.txt"  
num_lines = count_lines(filename)

if num_lines is not None:
    print(f"Number of lines in '{filename}': {num_lines}")
