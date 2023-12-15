import pygame
from sys import exit
from station import Station
from ground import Ground
from bullet import Bullet
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption('Planet Survivor')
clock = pygame.time.Clock()
game_active = True
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/sky.png').convert_alpha()
sky_red_surf = pygame.image.load(
    'graphics/sky_red.png').convert_alpha()

alpha = 0
sky_red_surf.set_alpha(alpha)
# ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
# ground_rect = ground_surf.get_rect(center=(0, 672))
ship_surf = pygame.image.load('graphics/ship/ship_merged.png').convert_alpha()
ship_rect = ship_surf.get_rect(midbottom=(300, 700))

station = pygame.sprite.GroupSingle()
station.add(Station(screen, 0))
lives = int(3)
# print(type(lives))

ground = pygame.sprite.GroupSingle()
ground.add(Ground())
# print(type(ground))

bullet_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()
enemy_speed = 1

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 400)

obstacle_timer2 = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer2, 1500)

score = 0
# score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(300, 400))


# def increase_dificulty(alpha, enemy_speed):
#     alpha += 10
#     if enemy_speed > 100:
#         enemy_speed = enemy_speed - 10
#     print(alpha, enemy_speed)


def display_score(score):
    score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(300, 50))
    screen.blit(score_surf, score_rect)


def display_lives():
    global lives
    single_life_surf = pygame.transform.scale2x(pygame.image.load(
        'graphics/player/life.png').convert_alpha())
    single_life_gray_surf = pygame.transform.scale2x(pygame.image.load(
        'graphics/player/life_grayed.png').convert_alpha())
    if lives == 3:
        screen.blit(single_life_surf, (10, 10))
        screen.blit(single_life_surf, (45, 10))
        screen.blit(single_life_surf, (80, 10))
    if lives == 2:
        screen.blit(single_life_surf, (10, 10))
        screen.blit(single_life_surf, (45, 10))
        screen.blit(single_life_gray_surf, (80, 10))
    if lives == 1:
        screen.blit(single_life_surf, (10, 10))
        screen.blit(single_life_gray_surf, (45, 10))
        screen.blit(single_life_gray_surf, (80, 10))
    if lives == 0:
        game_over()
    # else:
        # return print("error")


def collision_sprite(score):
    if pygame.sprite.groupcollide(bullet_group, enemy_group, False, True):
        score += 1
    return score


def collision_ground():
    global lives
    if pygame.sprite.groupcollide(ground, enemy_group, False, True):
        lives -= 1


def game_over():
    return


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                bullet_group.add(Bullet(screen, station.sprite.rot))
                alpha += 1
                enemy_speed += 0.01
                # print(enemy_speed)
                # increase_dificulty(alpha, enemy_speed)
                sky_red_surf.set_alpha(alpha)

            if event.type == obstacle_timer2:
                enemy_group.add(Enemy(screen))

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(sky_red_surf, (0, 0))
        display_lives()
        station.draw(screen)
        station.update()
        bullet_group.draw(screen)
        bullet_group.update()
        ground.draw(screen)
        enemy_group.draw(screen)
        enemy_group.update(enemy_speed)
        screen.blit(ship_surf, ship_rect)
        score = collision_sprite(score)
        collision_ground()
        display_score(score)

    pygame.display.update()
    clock.tick(60)
