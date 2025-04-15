import psycopg2

def setup_tables():
    conn = psycopg2.connect(
        host="localhost",
        database="assemmukhtarkyzy",
        user="assemmukhtarkyzy",
        password=""
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_user (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES game_user(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            paused_state TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

setup_tables()
print("Tables created ✅")
