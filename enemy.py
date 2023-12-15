import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        enemy = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
        self.pos_x = random.randint(10, 590)
        self.pos_y = 0
        self.image = enemy
        self.rect = self.image.get_rect(midbottom=(self.pos_x, self.pos_y))
        # print("Creating enemy")

    def movement(self, speed):
        self.pos_y += speed
        self.rect = self.image.get_rect(midbottom=(self.pos_x, self.pos_y))
        # print("Moving enemy")

    def destroy(self):
        if self.pos_y >= 750:
            self.kill()

    def update(self, speed):
        self.movement(speed)
        self.destroy()
