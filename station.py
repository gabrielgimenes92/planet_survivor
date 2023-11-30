import pygame


class Station(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        ship_background = pygame.image.load(
            'graphics/ship/ship_background.png').convert_alpha()
        # ship_cannon = pygame.image.load('graphics/ship/cannon.png').convert_alpha()
        # ship_background = pygame.draw.circle(
        #     screen, (217, 217, 217), (200, 690), 10)

        self.image = ship_background
        self.rect = self.image.get_rect(midbottom=(300, 750))
