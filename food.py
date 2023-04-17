import random
import pygame
from constants import SCREEN_WIDTH, BLOCK_SIZE, RED, GREY, BLACK, GAME_SURFACE_HEIGHT

# Definizione della classe Food
class Food:
    def __init__(self, num_fruits, bombs):
        self.num_fruits = num_fruits
        self.fruits = []
        # Carica l'immagine della frutta
        #self.fruit_image = pygame.image.load("apple.png")
        #self.fruit_image.set_colorkey(BLACK)        
        for i in range(num_fruits):
            self.spawn_fruit(bombs)

    def spawn_fruit(self, bombs):
        while True:
            x = random.randint(0, SCREEN_WIDTH/BLOCK_SIZE-1) * BLOCK_SIZE
            y = random.randint(0, (GAME_SURFACE_HEIGHT)/BLOCK_SIZE-1) * BLOCK_SIZE
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            if bombs == 0:
                # all'inizializzazione del gioco
                self.fruits.append(rect)
                break
            else:
                # Controlla che la frutta non si sovrapponga ad altre frutte o alle bombe
                if not any(rect.colliderect(fruit) for fruit in self.fruits) and not any(rect.colliderect(bomb) for bomb in bombs.bombs):
                    self.fruits.append(rect)
                    break

    def draw(self, screen):
        for fruit in self.fruits:
            # Usa un puntino rosso
            pygame.draw.rect(screen, RED, pygame.Rect(fruit.x, fruit.y, BLOCK_SIZE, BLOCK_SIZE))
            # Carica un'immagine
            # screen.blit(self.fruit_image, (fruit.x, fruit.y))

    def check_collision(self, snake):
        for fruit in self.fruits:
            if snake.rect.colliderect(fruit):
                self.fruits.remove(fruit)
                return True
        return False
        
# Definizione della classe Bomb   
class Bomb:
    def __init__(self,num_bombs, food):
        self.num_bombs = num_bombs
        self.bombs = []    
        # Carica l'immagine della bomba
        #self.bomb_image = pygame.image.load("bomb.png")
        #self.bomb_image.set_colorkey(BLACK)       
        for i in range(num_bombs):
            self.spawn_bomb(food)

    def spawn_bomb(self, food):
        # il ciclo while serve perché continuo a cercare un elemento valido finchè non smettono di sovrapporsi gli elementi
        while True:
            x = random.randint(0, SCREEN_WIDTH/BLOCK_SIZE-1) * BLOCK_SIZE
            y = random.randint(0, (GAME_SURFACE_HEIGHT)/BLOCK_SIZE-1) * BLOCK_SIZE
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            # Controlla che la bomba non si sovrapponga alla frutta o ad altre bombe
            if not any(rect.colliderect(fruit) for fruit in food.fruits) and not any(rect.colliderect(bomb) for bomb in self.bombs): 
                self.bombs.append(rect)
                break
    
    # Disegna le bombe 
    def draw(self, screen):
        for bomb in self.bombs:
            # Usa un puntino grigio
            pygame.draw.rect(screen, BLACK, pygame.Rect(bomb.x, bomb.y, BLOCK_SIZE, BLOCK_SIZE))

    # Verifica la collisione col serpente
    def check_collision(self, snake):
        for bomb in self.bombs:
            if snake.rect.colliderect(bomb):
                self.bombs.remove(bomb)
                return True
        return False
    
# Definizione della classe Obstacles   
class Obstacles:
    def __init__(self,num_obstacles):
        self.num_obstacles = num_obstacles
        self.obstacles = []    
        # Carica l'immagine dell'ostacolo
        #self.obst_image = pygame.image.load("obstacle.png")
        #self.obst_image.set_colorkey(GREY)       
        for i in range(num_obstacles):
            self.spawn_obstacles()

    def spawn_obstacles(self):
        # l'ostacolo è un elemento grande diverse block_size che può anche sovrapporsi agli altri oggetti
        # Genera un ostacolo
        obstacle = []
        length = random.randint(3, 6)  # Lunghezza dell'ostacolo
        x, y = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE), random.randint(0, GAME_SURFACE_HEIGHT - BLOCK_SIZE)
        direction = random.choice(["horizontal", "vertical"])  # Direzione dell'ostacolo
        if direction == "vertical":
            # Ostacolo orizzontale
            for i in range(length):
                obstacle.append([x + i * BLOCK_SIZE, y])
            # Aggiunge blocchi aggiuntivi all'ostacolo
            while True:
                if random.random() < 0.65 and y - BLOCK_SIZE >= 0 and [x, y - BLOCK_SIZE] not in obstacle:
                    # Aggiunge un blocco in alto
                    obstacle.insert(0, [x, y - BLOCK_SIZE])
                    y -= BLOCK_SIZE
                elif random.random() < 0.65 and y + BLOCK_SIZE * (length + 1) < GAME_SURFACE_HEIGHT and [x, y + BLOCK_SIZE * length] not in obstacle:
                    # Aggiunge un blocco in basso
                    obstacle.append([x, y + BLOCK_SIZE * length])
                else:
                    break
        else:
            # Ostacolo verticale
            for i in range(length):
                obstacle.append([x, y + i * BLOCK_SIZE])
            # Aggiunge blocchi aggiuntivi all'ostacolo
            while True:
                if random.random() < 0.65 and y - BLOCK_SIZE >= 0 and [x, y - BLOCK_SIZE] not in obstacle:
                    # Aggiunge un blocco a sinistra
                    obstacle.insert(0, [x - BLOCK_SIZE, y])
                    x -= BLOCK_SIZE
                elif random.random() < 0.65 and x + BLOCK_SIZE * (length + 1) < SCREEN_WIDTH and [x + BLOCK_SIZE * length, y] not in obstacle:
                    # Aggiunge un blocco a destra
                    obstacle.append([x + BLOCK_SIZE * length, y])
                else:
                    break

        # Aggiunge l'ostacolo alla lista degli ostacoli
        self.obstacles += obstacle
    
    # Disegna gli ostacoli 
    def draw(self, screen):
        for obstacle in self.obstacles:
            # Usa dei puntini grigio
            pygame.draw.rect(screen, GREY, pygame.Rect(obstacle[0], obstacle[1], BLOCK_SIZE, BLOCK_SIZE))
            
    # Verifica la collisione col serpente
    def check_collision(self, snake):
        obstacles_to_remove = []
        for obstacle in self.obstacles:
            if snake.rect.colliderect(pygame.Rect(obstacle[0], obstacle[1], BLOCK_SIZE, BLOCK_SIZE)):
                obstacles_to_remove.append(obstacle)
        for obstacle in obstacles_to_remove:
            self.obstacles.remove(obstacle)
        return len(obstacles_to_remove) > 0