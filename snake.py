import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, STARTING_DIRECTION, GREEN, STARTING_LIVES, INFO_SURFACE_HEIGHT, GAME_SURFACE_DISTANCE

# Definizione della classe Snake
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.rect = pygame.Rect(self.body[0][0], self.body[0][1], BLOCK_SIZE, BLOCK_SIZE)
        self.direction = STARTING_DIRECTION
        self.lives = STARTING_LIVES
        self.score = 0
        self.max_length = 1

    def move(self):
        x, y = self.body[0]
        if self.direction == "right":
            x += BLOCK_SIZE
        elif self.direction == "left":
            x -= BLOCK_SIZE
        elif self.direction == "up":
            y -= BLOCK_SIZE
        elif self.direction == "down":
            y += BLOCK_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()
        self.rect = pygame.Rect(self.body[0][0], self.body[0][1], BLOCK_SIZE, BLOCK_SIZE)

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def grow(self):
        x, y = self.body[0]
        if self.direction == "right":
            x += BLOCK_SIZE
        elif self.direction == "left":
            x -= BLOCK_SIZE
        elif self.direction == "up":
            y -= BLOCK_SIZE
        elif self.direction == "down":
            y += BLOCK_SIZE
        # aggiungi un pezzo alla coda
        self.body.insert(0, (x, y))
        self.rect = pygame.Rect(self.body[0][0], self.body[0][1], BLOCK_SIZE, BLOCK_SIZE)
        # aggiorna la max_length
        if len(self.body) > self.max_length:
            self.max_length = len(self.body)

    def check_tailEat_or_borderCollision(self):
        # verifica collisione con i bordi
        x, y = self.body[0]
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT - INFO_SURFACE_HEIGHT - GAME_SURFACE_DISTANCE or y > SCREEN_HEIGHT - INFO_SURFACE_HEIGHT - GAME_SURFACE_DISTANCE - BLOCK_SIZE:
            self.lives -= 1
            if self.lives == 0:
                return True
            else:
                self.reset()
                return False
        # verifica coda mangiata
        for i in range(1, len(self.body)):
            if self.body[i] == self.body[0]:
                self.lives -= 1
                if self.lives == 0:
                    return True
                else:
                    self.reset()
                    return False
        return False

    def reset(self):
        # Reimposta il serpente alle impostazioni iniziali dopo aver perso una vita
        self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.rect = pygame.Rect(self.body[0][0], self.body[0][1], BLOCK_SIZE, BLOCK_SIZE)
        self.direction = STARTING_DIRECTION
