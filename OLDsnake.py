import pygame
import random
import os 

# Inizializzazione di Pygame
pygame.init()

# Definizione delle costanti
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 10
FPS = 15
STARTING_LIVES = 3

# Creazione della finestra di gioco
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Definizione dei colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Definizione della classe Snake
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.direction = "right"
        self.lives = STARTING_LIVES

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

    def draw(self):
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
        self.body.insert(0, (x, y))

    def check_collision(self):
        x, y = self.body[0]
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives == 0:
                return True
            else:
                self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
                self.direction = "right"
                return False
        for i in range(1, len(self.body)):
            if self.body[i] == self.body[0]:
                self.lives -= 1
                if self.lives == 0:
                    return True
                else:
                    self.body = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
                    self.direction = "right"
                    return False
        return False
    
# Definizione della classe Food
class Food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH/BLOCK_SIZE-1) * BLOCK_SIZE
        self.y = random.randint(0, SCREEN_HEIGHT/BLOCK_SIZE-1) * BLOCK_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self, snake):
        if self.x == snake.body[0][0] and self.y == snake.body[0][1]:
            return True
        return False

# Funzione per la schermata iniziale
def show_start_screen():
    # Crea il font per il titolo
    title_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 50)
    # Crea il font per il testo di istruzioni
    instructions_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)

    # Crea il testo del titolo
    title_text = title_font.render("Snake Game", True, GREEN)
    # Crea il testo di istruzioni
    instructions_text = instructions_font.render("Press SPACE to start", True, WHITE)
    # Crea il testo per le vite
    lives_text = instructions_font.render("Lives: " + str(snake.lives), True, WHITE)
    
    # Disegna il titolo e il testo di istruzioni sulla schermata iniziale
    screen.fill(BLACK)
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, 100))
    screen.blit(lives_text, (SCREEN_WIDTH/2 - lives_text.get_width()/2, 200))
    screen.blit(instructions_text, (SCREEN_WIDTH/2 - instructions_text.get_width()/2, 300))

    # Aggiorna la finestra di gioco
    pygame.display.update()

    # Loop per la schermata iniziale
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Funzione per la schermata di Game Over
def show_game_over_screen():
    # Crea il font per il titolo
    title_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 50)

    # Crea il testo del titolo
    title_text = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)

    # Crea il font per il testo di istruzioni
    instructions_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)

    # Crea il testo delle vite rimanenti del serpente
    lives_text = instructions_font.render("Lives: " + str(snake.lives), True, WHITE)

    # Crea il testo di istruzioni
    instructions_text = instructions_font.render("Press SPACE to play again or ESC to quit", True, WHITE)

    # Disegna il titolo, il testo delle vite e il testo di istruzioni sulla schermata di Game Over
    screen.fill(BLACK)
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, 100))
    screen.blit(lives_text, (SCREEN_WIDTH/2 - lives_text.get_width()/2, 200))
    screen.blit(instructions_text, (SCREEN_WIDTH/2 - instructions_text.get_width()/2, 300))

    # Aggiorna la finestra di gioco
    pygame.display.update()

    # Loop per la schermata di Game Over
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Creazione del serpente e del cibo
snake = Snake()
food = Food()

# Definizione del clock
clock = pygame.time.Clock()

# Mostra la schermata iniziale
show_start_screen()

# Loop principale del gioco
game_over = False
while True:
    if game_over:
        show_game_over_screen()
        snake = Snake()
        food = Food()
        game_over = False
        
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"

    # Movimento del serpente
    snake.move()

    # Controllo delle collisioni
    if snake.check_collision():
        game_over = True
    if food.check_collision(snake):
        snake.grow()
        food = Food()

    # Disegno degli oggetti
    screen.fill(BLACK)
    snake.draw()
    food.draw()

    # Mostra il testo delle vite
    instructions_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)
    lives_text = instructions_font.render("Lives: " + str(snake.lives), True, WHITE)
    screen.blit(lives_text, (SCREEN_WIDTH/2 - lives_text.get_width()/2, 200))

    # Aggiornamento dello schermo
    pygame.display.update()

    # Controllo del framerate
    clock.tick(FPS)