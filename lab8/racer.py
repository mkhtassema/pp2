import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 300
LANE_WIDTH = ROAD_WIDTH // 3
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
COIN_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_speed = 5

coins = []
coin_spawn_timer = 0
coins_collected = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > WIDTH // 2 - ROAD_WIDTH // 2:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH // 2 + ROAD_WIDTH // 2 - PLAYER_WIDTH:
        player_x += player_speed
    
    coin_spawn_timer += 1
    if coin_spawn_timer > 50:
        coin_x = random.choice([WIDTH//2 - ROAD_WIDTH//2 + LANE_WIDTH//2, WIDTH//2, WIDTH//2 + ROAD_WIDTH//2 - LANE_WIDTH//2])
        coins.append([coin_x, 0])
        coin_spawn_timer = 0
    
    for coin in coins[:]:
        coin[1] += 5
        if coin[1] > HEIGHT:
            coins.remove(coin)
        if player_x < coin[0] < player_x + PLAYER_WIDTH and player_y < coin[1] < player_y + PLAYER_HEIGHT:
            coins.remove(coin)
            coins_collected += 1
    
    pygame.draw.rect(screen, BLACK, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
    
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), COIN_SIZE//2)
    
    text = font.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 20))
    
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()