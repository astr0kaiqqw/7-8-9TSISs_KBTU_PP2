import pygame
import random
import os

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game with Coins")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BASE_DIR = os.path.dirname(__file__)
car_image_path = os.path.join(BASE_DIR, "car.png")

if os.path.exists(car_image_path):
    car_img = pygame.image.load(car_image_path)
    car_img = pygame.transform.scale(car_img, (50, 80))  
    car_width, car_height = car_img.get_size()
else:
    car_img = None
    car_width, car_height = 50, 80 

class Car:
    def __init__(self):
        self.x = WIDTH // 2 - car_width // 2
        self.y = HEIGHT - car_height - 10
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - car_width:
            self.x += self.speed

    def draw(self):
        if car_img:
            screen.blit(car_img, (self.x, self.y))
        else:
            pygame.draw.rect(screen, RED, (self.x, self.y, car_width, car_height))  

class Coin:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -20
        self.speed = 4
        self.radius = 10

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

def check_collision(car, coin):
    if car.x < coin.x < car.x + car_width and car.y < coin.y < car.y + car_height:
        return True
    return False

running = True
clock = pygame.time.Clock()
car = Car()
coins = []
coin_spawn_time = 0
score = 0
font = pygame.font.Font(None, 36)

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.move("left")
    if keys[pygame.K_RIGHT]:
        car.move("right")

    if pygame.time.get_ticks() - coin_spawn_time > 1000:
        coins.append(Coin())
        coin_spawn_time = pygame.time.get_ticks()
    
    for coin in coins[:]:
        coin.move()
        coin.draw()
        if check_collision(car, coin):
            coins.remove(coin)
            score += 1
        elif coin.y > HEIGHT:
            coins.remove(coin)

    car.draw()

    score_text = font.render(f"Coins: {score}", True, RED)
    screen.blit(score_text, (WIDTH - 100, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()