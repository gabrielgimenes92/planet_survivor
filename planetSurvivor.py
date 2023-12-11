import pygame
from sys import exit
from station import Station
from bullet import Bullet
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Planet Survivor')
clock = pygame.time.Clock()
game_active = True
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ship_surf = pygame.image.load('graphics/ship/ship_merged.png').convert_alpha()
ship_rect = ship_surf.get_rect(midbottom=(300, 700))

station = pygame.sprite.GroupSingle()
station.add(Station(screen, 0))


bullet_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 400)

obstacle_timer2 = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer2, 1500)

score = 0
# score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(300, 400))


def display_score(score):
    score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(300, 50))
    screen.blit(score_surf, score_rect)


def collision_sprite(score):
    if pygame.sprite.groupcollide(bullet_group, enemy_group, False, True):
        score += 1
    return score


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                bullet_group.add(Bullet(screen, station.sprite.rot))

            if event.type == obstacle_timer2:
                enemy_group.add(Enemy(screen))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 690))
        station.draw(screen)
        station.update()
        bullet_group.draw(screen)
        bullet_group.update()
        enemy_group.draw(screen)
        enemy_group.update()
        screen.blit(ship_surf, ship_rect)
        score = collision_sprite(score)
        display_score(score)

    pygame.display.update()
    clock.tick(60)
