import json

# Caricamento delle costanti dal file JSON
with open("constants.json") as f:
    constants = json.load(f)

# Definizione delle costanti come variabili globali
SCREEN_WIDTH = constants["SCREEN_WIDTH"]
SCREEN_HEIGHT = constants["SCREEN_HEIGHT"]
BLOCK_SIZE = constants["BLOCK_SIZE"]
STARTING_FPS = constants["STARTING_FPS"]
STARTING_LIVES = constants["STARTING_LIVES"]
BLACK = constants["BLACK"]
WHITE = constants["WHITE"]
RED = constants["RED"]
GREEN = constants["GREEN"]
SNAKE_GREEN = constants["SNAKE_GREEN"]
GREY = constants["GREY"]
STARTING_DIRECTION = constants["STARTING_DIRECTION"]
NUM_FRUITS = constants["NUM_FRUITS"]
NUM_BOMB = constants["NUM_BOMB"]
NUM_OBSTACLES = constants["NUM_OBSTACLES"]
GAME_SURFACE_DISTANCE = constants["GAME_SURFACE_DISTANCE"]
INFO_SURFACE_HEIGHT = constants["INFO_SURFACE_HEIGHT"]
TEXT_DISTANCE = constants["TEXT_DISTANCE"]