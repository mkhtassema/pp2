import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0

pygame.mixer.music.load(music_files[current_track])

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill(WHITE)
    text = FONT.render(f"Now Playing: {music_files[current_track]}", True, (0, 0, 0))
    screen.blit(text, (50, HEIGHT // 2))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

pygame.quit()