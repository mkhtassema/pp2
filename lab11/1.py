import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="assemmukhtarkyzy",
        user="assemmukhtarkyzy",
        password=""
    )

# 1. Function: Поиск по шаблону
def search_by_pattern(pattern):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_users_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    print("\n--- Search Results ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    cur.close()
    conn.close()

# 2. Procedure: Добавление или обновление пользователя
def insert_or_update_user(name, phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Inserted or updated successfully!")
    cur.close()
    conn.close()

# 3. Procedure: Массовое добавление с проверкой номеров
def insert_many_users(names, phones):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    conn.commit()
    print("Inserted many users! (Check DB for invalid data)")
    cur.close()
    conn.close()

# 4. Function: Пагинация
def get_users_with_pagination(limit, offset):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users_with_pagination(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    print("\n--- Paginated Users ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    cur.close()
    conn.close()

# 5. Procedure: Удаление по имени или телефону
def delete_user(identifier):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CALL delete_user_by_identifier(%s)", (identifier,))
    conn.commit()
    print("User deleted (if existed).")
    cur.close()
    conn.close()

# Меню
def show_menu():
    print("\n--- PhoneBook Menu ---")
    print("1. Search by pattern")
    print("2. Insert or update user")
    print("3. Insert many users")
    print("4. Get users with pagination")
    print("5. Delete user")
    print("6. Exit")

# Главный цикл
while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        pattern = input("Enter name/phone pattern: ")
        search_by_pattern(pattern)

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        insert_or_update_user(name, phone)

    elif choice == "3":
        names = input("Enter names (comma separated): ").split(",")
        phones = input("Enter phones (comma separated): ").split(",")
        insert_many_users(names, phones)

    elif choice == "4":
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        get_users_with_pagination(limit, offset)

    elif choice == "5":
        identifier = input("Enter name or phone to delete: ")
        delete_user(identifier)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option!\n")