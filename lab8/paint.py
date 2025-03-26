import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

current_color = BLACK
mode = "pen"
drawing = False
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rectangle":
                end_pos = event.pos
                pygame.draw.rect(canvas, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle":
                end_pos = event.pos
                radius = ((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5
                pygame.draw.circle(canvas, current_color, start_pos, int(radius), 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pen":
                pygame.draw.line(canvas, current_color, event.pos, event.pos, 2)
            elif mode == "eraser":
                pygame.draw.line(canvas, WHITE, event.pos, event.pos, 10)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = BLUE
    
    screen.blit(canvas, (0, 0))
    pygame.display.flip()

pygame.quit()