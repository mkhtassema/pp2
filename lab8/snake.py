import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [[100, 100]]
direction = "RIGHT"
speed = 10
food = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]
score = 0
level = 1
font = pygame.font.Font(None, 36)

running = True
while running:
    pygame.time.delay(100 - speed)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    
    head = snake[0][:]
    if direction == "LEFT":
        head[0] -= GRID_SIZE
    if direction == "RIGHT":
        head[0] += GRID_SIZE
    if direction == "UP":
        head[1] -= GRID_SIZE
    if direction == "DOWN":
        head[1] += GRID_SIZE
    
    if head in snake or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False
    
    snake.insert(0, head)
    
    if head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
        food = [random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE)]
    else:
        snake.pop()
    
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()

pygame.quit()