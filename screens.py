import pygame
import datetime
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GREEN, SNAKE_GREEN, RED, GREY, BLOCK_SIZE, GAME_SURFACE_DISTANCE, TEXT_DISTANCE, INFO_SURFACE_HEIGHT

# Funzione per la schermata iniziale
def show_start_screen(screen):
    # Crea il font per il titolo
    title_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 50)

    # Crea il font per il testo di istruzioni
    instructions_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)

    # Crea il testo del titolo
    title_text = title_font.render("Snake Game", True, GREEN)

    # Crea il testo di istruzioni
    instructions_text1 = instructions_font.render("Use arrow keys to move", True, WHITE)
    instructions_text2 = instructions_font.render("Press SPACE to start", True, WHITE)

    # Disegna il titolo e il testo di istruzioni sulla schermata iniziale
    screen.fill(BLACK)
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, 100))
    screen.blit(instructions_text1, (SCREEN_WIDTH/2 - instructions_text1.get_width()/2, 300))
    screen.blit(instructions_text2, (SCREEN_WIDTH/2 - instructions_text2.get_width()/2, 340))

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

        # Aggiorna la finestra di gioco
        pygame.display.update()
             
# Funzione per la schermata di Game Over
def show_game_over_screen(screen, snake):
    # Crea il font per il titolo
    title_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 50)
    # Crea il font per il testo di istruzioni
    instructions_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 30)
    # Crea il font per la lunghezza massima ottenuto
    maxlength_font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 38)

    # Crea il testo del titolo
    title_text = title_font.render("GAME OVER!", True, GREEN)
    # Crea il testo delle vite rimanenti del serpente
    lives_text = instructions_font.render("Lives: " + str(snake.lives), True, WHITE)
    # Crea il testo del punteggio del serpente
    score_text = instructions_font.render("Score: " + str(snake.score), True, WHITE)
    # Crea il testo di istruzioni con due righe separate
    instructions_text1 = instructions_font.render("Press SPACE to play again", True, WHITE)
    instructions_text2 = instructions_font.render("or ESC to quit", True, WHITE)
    # Crea il testo per la lunghezza massima del serpente
    maxlength_text = maxlength_font.render("Max Length: " + str(snake.max_length), True, GREEN)

    # Disegna il testo di istruzioni sulla schermata di Game Over
    screen.fill(BLACK)
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, 100))
    screen.blit(lives_text, (SCREEN_WIDTH/2 - lives_text.get_width()/2, 200))
    screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, 240))
    screen.blit(instructions_text1, (SCREEN_WIDTH/2 - instructions_text1.get_width()/2, 300))
    screen.blit(instructions_text2, (SCREEN_WIDTH/2 - instructions_text2.get_width()/2, 340))
    screen.blit(maxlength_text, (SCREEN_WIDTH/2 - instructions_text2.get_width()/2, 400))

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
                    
# Funzione per disegnare la schermata di gioco
def draw_screen(screen, snake, food, bombs, obstacles):

    # Disegna lo sfondo
    screen.fill(BLACK)

    # Crea la superficie di gioco
    game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - INFO_SURFACE_HEIGHT - GAME_SURFACE_DISTANCE))

    # Riempie la superficie di gioco di verde
    game_surface.fill(GREEN)
    
    # Disegna il serpente sulla la superficie di gioco
    for body in snake.body:
        pygame.draw.rect(game_surface, SNAKE_GREEN, pygame.Rect(body[0], body[1], BLOCK_SIZE, BLOCK_SIZE))

    # Disegna bombe, frutta e ostacoli sulla superficie di gioco
    bombs.draw(game_surface)
    food.draw(game_surface)
    obstacles.draw(game_surface)
    
    # Disegna la superficie di gioco sulla finestra principale
    screen.blit(game_surface, (0, GAME_SURFACE_DISTANCE))

    # Disegna il contorno bianco all'interno del rettangolo nero
    contour_thickness = 2
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, GAME_SURFACE_DISTANCE, SCREEN_WIDTH, SCREEN_HEIGHT - INFO_SURFACE_HEIGHT - GAME_SURFACE_DISTANCE), contour_thickness)

    # Crea la superficie delle informazioni
    info_surface = pygame.Surface((SCREEN_WIDTH, INFO_SURFACE_HEIGHT))
    info_surface.fill(BLACK)

    # Crea il font per il testo delle vite, del punteggio, dei frutti, delle bombe, della lunghezza del serpente e del tempo
    font = pygame.font.Font(os.path.join("fonts", "PressStart2P-Regular.ttf"), 20)

    # Disegna il testo delle vite sulla finestra di gioco
    lives_text = font.render("Lives: " + str(snake.lives), True, WHITE)
    screen.blit(lives_text, (10, 10))

    # Disegna il punteggio sulla finestra di gioco
    score_text = font.render("Score: " + str(snake.score), True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - TEXT_DISTANCE, TEXT_DISTANCE))

    # Disegna la lunghezza del serpente sulla superficie delle informazioni
    length_text = font.render("Max Length: " + str(snake.max_length), True, WHITE)
    length_text_rect = length_text.get_rect(left=TEXT_DISTANCE, centery=INFO_SURFACE_HEIGHT//2)
    info_surface.blit(length_text, length_text_rect)

    # Disegna il tempo sulla superficie delle informazioni
    time = datetime.datetime.fromtimestamp(pygame.time.get_ticks() / 1000)
    if time.microsecond % 1000 == 0:
        time_text = font.render("Time: " + time.strftime("%M:%S") + ".{:03d}".format(time.microsecond // 1000), True, WHITE)
    else:
        time_text = font.render("Time: " + time.strftime("%M:%S.") + str(time.microsecond // 1000).ljust(3, "0"), True, WHITE)
    time_text_rect = time_text.get_rect(right=SCREEN_WIDTH - TEXT_DISTANCE, centery=INFO_SURFACE_HEIGHT//2)
    info_surface.blit(time_text, time_text_rect)

    # Disegna il numero di frutti al centro in alto
    num_fruits = len(food.fruits)
    fruits_text = font.render("Fruits: " + str(num_fruits), True, WHITE)
    fruits_text_rect = fruits_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
    screen.blit(fruits_text, fruits_text_rect)

    # Disegna il numero di bombe al centro in alto
    num_bombs = len(bombs.bombs)
    bombs_text = font.render("Bombs: " + str(num_bombs), True, WHITE)
    bombs_text_rect = bombs_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(bombs_text, bombs_text_rect)

    # Disegna la superficie delle informazioni sulla finestra di gioco
    screen.blit(info_surface, (0, SCREEN_HEIGHT - INFO_SURFACE_HEIGHT))

    # Aggiorna la finestra di gioco
    pygame.display.update()