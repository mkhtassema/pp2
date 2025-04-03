import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

car = pygame.image.load("/Users/assemmukhtarkyzy/Desktop/pp2/lab9/player.png")
enemy = pygame.image.load("/Users/assemmukhtarkyzy/Desktop/pp2/lab9/enemy.png")
coin_img = pygame.image.load("/Users/assemmukhtarkyzy/Desktop/pp2/lab9/coin.png")

car = pygame.transform.scale(car, (50, 100))
enemy = pygame.transform.scale(enemy, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))

car_x, car_y = WIDTH // 2 - 25, HEIGHT - 120
car_speed = 5

enemy_x, enemy_y = random.randint(50, WIDTH - 50), -100
enemy_speed = 3

coins = []
coin_weights = [1, 2, 3]
coin_speed = 3
score = 0
N = 10

def generate_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-300, -50)
    weight = random.choice(coin_weights)
    return [x, y, weight]

for _ in range(5):
    coins.append(generate_coin())

running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 50)
    
    for coin in coins:
        coin[1] += coin_speed
        if coin[1] > HEIGHT:
            coins.remove(coin)
            coins.append(generate_coin())
    
    car_rect = pygame.Rect(car_x, car_y, 50, 100)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 100)
    
    if car_rect.colliderect(enemy_rect):
        print("Game Over!")
        running = False
    
    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1], 30, 30)
        if car_rect.colliderect(coin_rect):
            score += coin[2]
            coins.remove(coin)
            coins.append(generate_coin())
    
    if score >= N:
        enemy_speed = 5
    
    screen.blit(car, (car_x, car_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    for coin in coins:
        screen.blit(coin_img, (coin[0], coin[1]))
    
    pygame.display.update()

pygame.quit()
