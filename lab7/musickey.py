import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "music"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_song = 1
if not songs:
    print("Нет файлов в папке!")
    exit()


def play_song():
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song]))
    pygame.mixer.music.play()

play_song()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)
running = True
paused = False

while running:
    screen.fill((30, 30, 30))
    
    text = font.render(f"Playing: {songs[current_song]}", True, (255, 255, 255))
    screen.blit(text, (20, 80))
    

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_song()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                paused = False
            elif event.key == pygame.K_n:  # Next song
                current_song = (current_song + 1) % len(songs)
                play_song()
                paused = False
            elif event.key == pygame.K_b:  # Previous song
                current_song = (current_song - 1) % len(songs)
                play_song()
                paused = False
                

pygame.quit()
