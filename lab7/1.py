import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)

background = pygame.image.load("clock_face.png")
minute_hand = pygame.image.load("mickey_right_hand.png")
second_hand = pygame.image.load("mickey_left_hand.png")

minute_hand = pygame.transform.scale(minute_hand, (200, 50))
second_hand = pygame.transform.scale(second_hand, (200, 50))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

running = True
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    minute_angle = -(minutes % 60) * 6
    second_angle = -(seconds % 60) * 6
    
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    
    minute_rect = rotated_minute.get_rect(center=CENTER)
    second_rect = rotated_second.get_rect(center=CENTER)
    
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()