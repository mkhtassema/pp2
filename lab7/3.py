import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
BALL_SPEED = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
                ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
                ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
                ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
                ball_x += BALL_SPEED

pygame.quit()