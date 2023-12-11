import math
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, rot):
        super().__init__()
        self.rot = rot + 90
        x_initial = 300
        y_initial = 685
        radians = math.radians(self.rot)
        self.offset = 5
        offset_initial = 100
        self.x = x_initial + math.cos(radians)*offset_initial
        self.y = y_initial - math.sin(radians)*offset_initial
        self.image = pygame.image.load('graphics/bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # print("Bullet created")

    def fire(self):
        radians = math.radians(self.rot)
        # print(radians)

        # print(self.x, self.y)
        self.x += math.cos(radians)*self.offset
        self.y -= math.sin(radians)*self.offset
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # print(self.x, self.y)

    def destroy(self):
        if self.x >= 1000 or self.x <= -1000:
            # print("Bullet destroyed")
            self.kill()

    def update(self):
        self.fire()
        self.destroy()
