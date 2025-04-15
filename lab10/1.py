import psycopg2
import csv

# Connect to PostgreSQL
def connect():
    return psycopg2.connect(
        host="localhost",
        database="assemmukhtarkyzy",
        user="assemmukhtarkyzy",
        password=""
    )

# Upload data from CSV
def upload_data_from_csv():
    try:
        with open('/Users/assemmukhtarkyzy/Desktop/pp2/lab10/phonebook.csv', 'r') as f:
            reader = csv.DictReader(f)
            conn = connect()
            cur = conn.cursor()
            for row in reader:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))
            conn.commit()
            cur.close()
            conn.close()
            print("Data uploaded from CSV ✅")
    except FileNotFoundError:
        print("CSV file not found ❌")

# Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted ✅")

# Update data
def update_data():
    name = input("Enter existing username to update: ")
    new_name = input("New name (leave blank to skip): ")
    new_phone = input("New phone (leave blank to skip): ")

    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE phonebook SET first_name=%s WHERE first_name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE first_name=%s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Updated successfully ✅")

# Query with filters
def query_data():
    print("1. Show all\n2. Filter by name\n3. Filter by phone")
    option = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if option == '1':
        cur.execute("SELECT * FROM phonebook")
    elif option == '2':
        name = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif option == '3':
        phone = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# Delete by username or phone
def delete_data():
    print("1. Delete by username\n2. Delete by phone")
    option = input("Choose: ")

    conn = connect()
    cur = conn.cursor()

    if option == '1':
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))
    elif option == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted successfully ✅")

# MAIN MENU
def main():
    while True:
        print("\nPhonebook Menu:")
        print("1. Upload data from CSV")
        print("2. Insert data from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")

        choice = input("Enter choice: ").strip()  # Убираем лишние пробелы

        if not choice.isdigit():  # Если введено не число, выводим сообщение
            print("Invalid input! Please enter a number from the menu.")
            continue

        print(f"User input: '{choice}'")  # Выводим, что пользователь ввел

        if choice == '1':
            upload_data_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice ❌")

if __name__ == "__main__":
    main()
