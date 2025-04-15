import pygame, random, psycopg2

# ---------------- DATABASE FUNCTIONS ----------------
def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="assemmukhtarkyzy",
        user="assemmukhtarkyzy",
        password=""
    )

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM game_user WHERE username=%s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO game_user (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT score, level FROM user_score WHERE user_id=%s", (user_id,))
    score_data = cur.fetchone()

    if score_data:
        score, level = score_data
    else:
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        score, level = 0, 1

    cur.close()
    conn.close()
    return user_id, score, level

def save_score(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE user_score SET score=%s, level=%s WHERE user_id=%s
    """, (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

# ---------------- GAME CONFIG ----------------
CELL_SIZE = 20
WIDTH, HEIGHT = 600, 400
FPS_BASE = 5

# ---------------- GAME INIT ----------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# ---------------- LEVEL SETTINGS ----------------
walls_by_level = {
    1: [],
    2: [(300, y) for y in range(0, HEIGHT, CELL_SIZE)],
    3: [(x, 200) for x in range(0, WIDTH, CELL_SIZE)],
}
speed_by_level = {1: 5, 2: 7, 3: 10}

# ---------------- MAIN ----------------
username = input("Enter username: ")
user_id, score, level = get_or_create_user(username)
print(f"Welcome {username}! Level: {level}, Score: {score}")

snake = [(100, 100)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

running = True
paused = False

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, (128, 128, 128), (*wall, CELL_SIZE, CELL_SIZE))

while running:
    clock.tick(speed_by_level.get(level, FPS_BASE))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_score(user_id, score, level)
                    print("Game paused & saved to DB.")
            elif event.key == pygame.K_UP: direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN: direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT: direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT: direction = (CELL_SIZE, 0)

    if paused:
        continue

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    if head == food:
        score += 1
        if score % 3 == 0 and level < 3:
            level += 1
        food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        snake.pop()

    if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or
        head in snake[1:] or head in walls_by_level.get(level, [])):
        save_score(user_id, score, level)
        print("Game over. Score saved.")
        running = False

    # DRAW
    screen.fill((0, 0, 0))
    draw_walls(walls_by_level.get(level, []))
    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL_SIZE, CELL_SIZE))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*s, CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()
