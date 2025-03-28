import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)
clock = pygame.time.Clock()

current_color = BLACK
brush_size = 5
mode = "brush"

def draw_circle(pos):
    pygame.draw.circle(screen, current_color, pos, brush_size)

def draw_rectangle(pos):
    rect_size = brush_size * 2
    pygame.draw.rect(screen, current_color, (pos[0] - rect_size // 2, pos[1] - rect_size // 2, rect_size, rect_size))

def erase(pos):
    pygame.draw.circle(screen, WHITE, pos, brush_size * 2)

def draw_triangle(pos):
    size = brush_size * 2
    points = [
        (pos[0], pos[1] - size),
        (pos[0] - size, pos[1] + size),
        (pos[0] + size, pos[1] + size),
    ]
    pygame.draw.polygon(screen, current_color, points)

def draw_equilateral_triangle(pos):
    size = brush_size * 2
    height = math.sqrt(3) * size / 2
    points = [
        (pos[0], pos[1] - height),
        (pos[0] - size, pos[1] + height),
        (pos[0] + size, pos[1] + height),
    ]
    pygame.draw.polygon(screen, current_color, points)

def draw_rhombus(pos):
    size = brush_size * 2
    points = [
        (pos[0], pos[1] - size),
        (pos[0] - size, pos[1]),
        (pos[0], pos[1] + size),
        (pos[0] + size, pos[1]),
    ]
    pygame.draw.polygon(screen, current_color, points)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "rectangle"
            elif event.key == pygame.K_t:
                mode = "triangle"
            elif event.key == pygame.K_u:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_p:
                mode = "brush"
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if mode == "brush":
                draw_circle(event.pos)
            elif mode == "circle":
                draw_circle(event.pos)
            elif mode == "rectangle":
                draw_rectangle(event.pos)
            elif mode == "eraser":
                erase(event.pos)
            elif mode == "triangle":
                draw_triangle(event.pos)
            elif mode == "equilateral_triangle":
                draw_equilateral_triangle(event.pos)
            elif mode == "rhombus":
                draw_rhombus(event.pos)
    
    pygame.display.update() 
    clock.tick(60)

pygame.quit()
