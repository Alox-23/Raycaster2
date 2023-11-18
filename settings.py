import math

RES = WIDTH, HEIGHT = 1000, 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = WIDTH // 2
FPS = 30

PLAYER_POS = 27, 15
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_VERT_ROT_SPEED = 0.75

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL = 45 
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_TOP = 100
MOUSE_BORDER_BOTTOM = HEIGHT - MOUSE_BORDER_TOP

FOV = 1.2
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 150
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2