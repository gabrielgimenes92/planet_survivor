import math
import pygame


class Station(pygame.sprite.Sprite):

    def __init__(self, screen, rot):
        super().__init__()
        # ship_background = pygame.image.load(
        #     'graphics/ship/ship_background.png').convert_alpha()
        # ship_cannon = pygame.image.load(
        #     'graphics/ship/ship_cannon.png').convert_alpha()
        ship = pygame.image.load(
            'graphics/ship/ship_cannon.png').convert_alpha()
        self.image = ship
        self.rect = self.image.get_rect(center=(300, 685))
        self.rot = rot
        self.rot_speed = 1
        self.lives = 2

    def station_input(self):
        keys = pygame.key.get_pressed()
        ship = pygame.image.load(
            'graphics/ship/ship_cannon.png').convert_alpha()

        if keys[pygame.K_RIGHT] and self.rot >= -80:
            if self.rot > -30:
                self.rot -= self.rot_speed
                self.image = pygame.transform.rotate(ship, self.rot)
                self.rect = self.image.get_rect(center=(300, 685))
            else:
                self.rot -= self.rot_speed
                self.image = pygame.transform.rotate(ship, self.rot)
                self.rect = self.image.get_rect(center=(299, 685))

        if keys[pygame.K_LEFT] and self.rot <= 80:
            self.rot += self.rot_speed
            self.image = pygame.transform.rotate(ship, self.rot)
            self.rect = self.image.get_rect(center=(300, 685))

        if keys[pygame.K_SPACE] and self.rot_speed <= 3:
            self.rot_speed += 0.1
            # print(self.rot_speed)

        # if keys[pygame.K_f]:
        #     self.fire()

    # def get_rot(self):
    #     return self.rot

    def update(self):
        self.station_input()
