from settings import *
import pygame
import math
 
class PLAYER:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.vert_angle = 0
        self.floor = 0
        self.z = 750
        self.height = 750
        self.jump_power = 150
        self.gravity = 20
        self.vel_z = 0
        self.can_jump = True

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map[self.floor]

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx 
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def check_floor(self):
        self.floor = self.z//500
        if self.floor < 0:
            self.floor = 0

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        if keys[pygame.K_r]:
            self.z += 10
        if keys[pygame.K_f]:
            self.z -= 10

        if keys[pygame.K_SPACE] and self.can_jump:
            self.vel_z = self.jump_power
            self.can_jump = False

        if self.z > self.height:
            self.vel_z -= self.gravity
        else:
            self.can_jump = True
            if self.vel_z < 0:
                self.vel_z = 0
        print(self.height, self.z)
        
        self.z += self.vel_z


        self.check_wall_collision(dx, dy)


    def draw(self):

        pygame.draw.circle(self.game.screan, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        if my < MOUSE_BORDER_TOP or my > MOUSE_BORDER_BOTTOM:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pygame.mouse.get_rel()
        self.relx = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel[0]))
        self.angle += self.relx * MOUSE_SENSITIVITY * self.game.delta_time

        self.rely = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel[1]))
        self.vert_angle += self.rely * 0.3 * self.game.delta_time
        
        if self.vert_angle > 700:
            self.vert_angle = 700
        if self.vert_angle < -500:
            self.vert_angle = -500
        
        




    def update(self):
        self.movement()
        self.check_floor()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

