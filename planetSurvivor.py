import pygame
from sys import exit
from station import Station

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Planet Survivor')
clock = pygame.time.Clock()
game_active = True

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
station = pygame.sprite.GroupSingle()
station.add(Station(screen))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 690))

        station.draw(screen)

    pygame.display.update()
    clock.tick(60)
