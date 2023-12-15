import pygame


class Ground(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        ground = pygame.image.load('graphics/ground.png').convert_alpha()
        self.image = ground
        self.rect = self.image.get_rect(midbottom=(300, 800))
