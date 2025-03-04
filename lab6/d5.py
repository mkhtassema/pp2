def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')  
        print(f"List successfully written to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

my_list = ["Apple", "Banana", "Cherry", "Date"]
filename = "output.txt"
write_list_to_file(filename, my_list)
