import pygame
from settings import *


class ObjectRenderer:

    def __init__(self, game):
        self.game = game
        self.screan = game.screan
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.ray.objects_to_render
        for depth, img, pos in list_objects:
            self.screan.blit(img, (pos[0], pos[1]))

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('walllower.png'),
            2: self.get_texture('wallupper.png'),
            3: self.get_texture("chalk.png")
        }
