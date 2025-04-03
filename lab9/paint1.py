import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

shapes = []
current_shape = None
shape_type = "rectangle"

def draw_square(start, end):
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    return pygame.Rect(start[0], start[1], side, side)

def draw_right_triangle(start, end):
    return [start, (start[0], end[1]), end]

def draw_equilateral_triangle(start, end):
    side = abs(end[0] - start[0])
    height = int((math.sqrt(3) / 2) * side)
    return [(start[0], start[1] + height), (start[0] + side, start[1] + height), ((start[0] + end[0]) // 2, start[1])]

def draw_rhombus(start, end):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    return [(start[0] + width // 2, start[1]), (end[0], start[1] + height // 2), (start[0] + width // 2, end[1]), (start[0], start[1] + height // 2)]

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape_type = "rectangle"
            elif event.key == pygame.K_2:
                shape_type = "square"
            elif event.key == pygame.K_3:
                shape_type = "right_triangle"
            elif event.key == pygame.K_4:
                shape_type = "equilateral_triangle"
            elif event.key == pygame.K_5:
                shape_type = "rhombus"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_shape = [event.pos]
        elif event.type == pygame.MOUSEBUTTONUP:
            current_shape.append(event.pos)
            if shape_type == "rectangle":
                shapes.append(("rect", pygame.Rect(*current_shape[0], *(current_shape[1][0] - current_shape[0][0], current_shape[1][1] - current_shape[0][1]))))
            elif shape_type == "square":
                shapes.append(("rect", draw_square(current_shape[0], current_shape[1])))
            elif shape_type == "right_triangle":
                shapes.append(("polygon", draw_right_triangle(current_shape[0], current_shape[1])))
            elif shape_type == "equilateral_triangle":
                shapes.append(("polygon", draw_equilateral_triangle(current_shape[0], current_shape[1])))
            elif shape_type == "rhombus":
                shapes.append(("polygon", draw_rhombus(current_shape[0], current_shape[1])))
            current_shape = None
    
    for shape in shapes:
        if shape[0] == "rect":
            pygame.draw.rect(screen, BLACK, shape[1], 2)
        elif shape[0] == "polygon":
            pygame.draw.polygon(screen, BLACK, shape[1], 2)
    
    pygame.display.update()

pygame.quit()
