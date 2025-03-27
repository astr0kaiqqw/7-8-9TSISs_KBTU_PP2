import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE
        
        new_head = (head_x, head_y)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        self.body.insert(0, new_head)

    def check_collision(self):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        if (head_x, head_y) in self.body[1:]:
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_food(snake_body)
        self.spawn_time = time.time()  # время появления еды
        self.weight = random.randint(1, 3)  # вес еды (от 1 до 3)

    def generate_food(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

    def is_expired(self):
        # Еда исчезает через 5 секунд
        return time.time() - self.spawn_time > 5

running = True
clock = pygame.time.Clock()
snake = Snake()
food = Food(snake.body)
score = 0
font = pygame.font.Font(None, 30)

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake.direction != "DOWN":
        snake.direction = "UP"
    if keys[pygame.K_DOWN] and snake.direction != "UP":
        snake.direction = "DOWN"
    if keys[pygame.K_LEFT] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    if keys[pygame.K_RIGHT] and snake.direction != "LEFT":
        snake.direction = "RIGHT"
    
    snake.move()
    
    if snake.check_collision():
        running = False
    
    if snake.body[0] == food.position:
        snake.grow = True
        score += food.weight
        food = Food(snake.body)
    
    if food.is_expired():
        food = Food(snake.body)

    snake.draw()
    food.draw()
    
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(10)

pygame.quit()
