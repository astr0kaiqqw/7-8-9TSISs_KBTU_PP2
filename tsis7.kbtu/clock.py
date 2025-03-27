import pygame
import os
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Project")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_x, ball_y = WIDTH // 2, HEIGHT // 2
BALL_RADIUS = 25
BALL_SPEED = 20

pygame.mixer.init()
MUSIC_FOLDER = os.path.join(os.path.dirname(__file__), "music")
if not os.path.exists(MUSIC_FOLDER):
    os.makedirs(MUSIC_FOLDER)
music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_track = 0
print("Music files found:", music_files)

def play_music():
    if music_files:
        print("Playing:", music_files[current_track]) 
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, music_files[current_track]))
        pygame.mixer.music.play()
    else:
        print("No music files found!")

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    if music_files:
        current_track = (current_track + 1) % len(music_files)
        play_music()

def prev_track():
    global current_track
    if music_files:
        current_track = (current_track - 1) % len(music_files)
        play_music()

clock_face = pygame.image.load(os.path.join(os.path.dirname(__file__), "mickeyclock.jpeg"))
clock_face = pygame.transform.scale(clock_face, (200, 200))
clock_rect = clock_face.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    now = datetime.datetime.now()
    minute_angle = -(now.minute * 6)  
    second_angle = -(now.second * 6)
    
    screen.blit(clock_face, clock_rect)
    
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                prev_track()
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_UP and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
                ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + BALL_SPEED <= HEIGHT:
                ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
                ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + BALL_SPEED <= WIDTH:
                ball_x += BALL_SPEED
    
    clock.tick(30)
pygame.quit()