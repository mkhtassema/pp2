# phonebook_setup.py
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="assemmukhtarkyzy",
    user="assemmukhtarkyzy",
    password=""
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    phone VARCHAR(20)
);
""")

conn.commit()
cur.close()
conn.close()

print("PhoneBook table created ✅")
