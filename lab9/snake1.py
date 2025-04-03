import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
snake_speed = 100
food_items = []
food_weights = {1: GREEN, 3: RED}

def generate_food():
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    weight = random.choice(list(food_weights.keys()))
    lifetime = random.randint(3000, 7000)
    return [x, y, weight, pygame.time.get_ticks() + lifetime]

for _ in range(3):
    food_items.append(generate_food())

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN]:
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT]:
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT]:
        snake_dir = (CELL_SIZE, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)
    
    for food in food_items[:]:
        if new_head == (food[0], food[1]):
            snake.extend([(0, 0)] * (food[2] - 1))
            food_items.remove(food)
            food_items.append(generate_food())
        elif pygame.time.get_ticks() > food[3]:
            food_items.remove(food)
            food_items.append(generate_food())
    
    snake.pop()
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    for food in food_items:
        pygame.draw.rect(screen, food_weights[food[2]], (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    pygame.display.update()
    clock.tick(snake_speed // 10)

pygame.quit()
