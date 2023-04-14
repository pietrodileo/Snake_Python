import pygame
import random
import os 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, STARTING_FPS, NUM_FRUITS, NUM_BOMB, NUM_OBSTACLES, WHITE, BLACK
from snake import Snake
from food import Food, Bomb, Obstacles
from screens import show_start_screen, show_game_over_screen, draw_screen

def init_game(num_fruits, num_bombs, num_obstacles):
    snake = Snake()
    food = Food(num_fruits, 0)
    bombs = Bomb(num_bombs, food)
    obstacles = Obstacles(num_obstacles)
    food.bombs = bombs
    game_over = False
    num_fruits_eaten = 0
    fps = STARTING_FPS
    speed_up_timer = -800
    newLife_timer = -800
    return food, bombs, obstacles, snake, game_over, num_fruits_eaten, fps, speed_up_timer, newLife_timer

# Inizializzazione di Pygame
pygame.init()

# Creazione della finestra di gioco
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Definizione del clock
clock = pygame.time.Clock()

# Inizializzazione del gioco e creazione del serpente, del cibo e delle bombe
food, bombs, obstacles, snake, game_over, num_fruits_eaten, \
    fps, speed_up_timer,newLife_timer = init_game(NUM_FRUITS, NUM_BOMB, NUM_OBSTACLES)

# Mostra la schermata iniziale
show_start_screen(screen)

# Loop principale del gioco
while True:
    if game_over:
        show_game_over_screen(screen, snake)
        # resetto i parametri per un eventuale New Game 
        food, bombs, snake, game_over, num_fruits_eaten,\
            fps, speed_up_timer, newLife_timer = init_game(NUM_FRUITS, NUM_BOMB, NUM_OBSTACLES)
    
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            # Se l'utente preme ESC esci dal gioco
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            # Controllo della direzione del serpente
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
    if snake.check_tailEat_or_borderCollision():
        # se il serpente si mangia la coda o se colpisce i bordi
        game_over = True
    
    # se il serpente mangia un frutto
    if food.check_collision(snake):
        snake.grow()
        # crea un frutto che sostituisce quello mangiato
        food.spawn_fruit(bombs)
        # aumento il punteggio 
        snake.score += 10
        # Aumenta il numero delle bombe man mano che il serpente cresce
        num_fruits_eaten += 1
        # ogni 2 frutti mangiati inserisci una nuova bomba
        if num_fruits_eaten % 2 == 0:
            bombs.spawn_bomb(food)  
        # ogni 3 frutti mangiati inserisci un nuovo frutto
        if num_fruits_eaten % 3 == 0:
            food.spawn_fruit(bombs) 
        # aggiunge un grosso ostacolo ogni 4 frutti mangiati
        if num_fruits_eaten % 4 == 0:
            obstacles.spawn_obstacles() 
        # aumenta la velocità del gioco ogni 5 frutti mangiati
        if num_fruits_eaten % 4 == 0:
            fps += 3 
            SpeedUpfont = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)
            speed_up_timer = pygame.time.get_ticks()
            speed_up_text = SpeedUpfont.render("Speed Up!!!", True, BLACK)
        # aumenta una vita ogni 10 frutti mangiati
        if num_fruits_eaten % 10 == 0:
            snake.lives += 1
            newLife_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 40)
            newLife_timer = pygame.time.get_ticks()
            newLife_text = newLife_font.render("NEW LIFE!!!", True, WHITE)

    # se il serpente mangia una bomba
    if bombs.check_collision(snake):
        snake.lives -= 1
        if snake.lives > 0:
            snake.reset()
        else:
            game_over = True

    # se il serpente mangia una bomba
    if obstacles.check_collision(snake):
        snake.lives -= 1
        if snake.lives > 0:
            snake.reset()
        else:
            game_over = True

    # Disegna gli oggetti sullo schermo
    draw_screen(screen, snake, food, bombs, obstacles)
    
    # Scrivi Speed Up!! ad ogni aumento di velocità se il timer è attivo
    if pygame.time.get_ticks() - speed_up_timer < 800:
        screen.blit(speed_up_text, (SCREEN_WIDTH // 2 - speed_up_text.get_width() // 2, SCREEN_HEIGHT // 2 - speed_up_text.get_height() // 2))
    
    # Scrivi New Life!! 
    if pygame.time.get_ticks() - newLife_timer < 800:
        screen.blit(newLife_text, (SCREEN_WIDTH // 2 - newLife_text.get_width() // 2, SCREEN_HEIGHT // 2 - newLife_text.get_height() // 2))

    # Aggiornamento dello schermo
    pygame.display.update()

    # Controllo del framerate
    clock.tick(fps)