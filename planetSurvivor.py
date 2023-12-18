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
global game_over
game_over = False
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/sky.png').convert_alpha()
sky_red_surf = pygame.image.load(
    'graphics/sky_red.png').convert_alpha()

alpha = 0
sky_red_surf.set_alpha(alpha)
ship_surf = pygame.image.load('graphics/ship/ship_merged.png').convert_alpha()
ship_rect = ship_surf.get_rect(midbottom=(300, 700))

station = pygame.sprite.GroupSingle()
station.add(Station(screen, 0))
lives = int(3)

ground = pygame.sprite.GroupSingle()
ground.add(Ground())

bullet_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()
enemy_speed = 1

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 400)

obstacle_timer2 = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer2, 1500)

score = 0

# def increase_dificulty(alpha, enemy_speed):
#     alpha += 10
#     if enemy_speed > 100:
#         enemy_speed = enemy_speed - 10
#     print(alpha, enemy_speed)


def display_score(score, message, position):
    score_surf = test_font.render(f'{message}{score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(position))
    screen.blit(score_surf, score_rect)


def display_lives():
    global lives
    single_life_surf = pygame.transform.scale2x(pygame.image.load(
        'graphics/player/life.png').convert_alpha())
    single_life_gray_surf = pygame.transform.scale(pygame.image.load(
        'graphics/player/life_grayed.png').convert_alpha(), (25, 25))
    pos_one_rect = single_life_surf.get_rect(center=(20, 20))
    pos_two_rect = single_life_surf.get_rect(center=(55, 20))
    pos_three_rect = single_life_surf.get_rect(center=(90, 20))
    pos_two_gray_rect = single_life_gray_surf.get_rect(center=(55, 20))
    pos_three_gray_rect = single_life_gray_surf.get_rect(center=(90, 20))

    if lives == 3:
        screen.blit(single_life_surf, pos_one_rect)
        screen.blit(single_life_surf, pos_two_rect)
        screen.blit(single_life_surf, pos_three_rect)
    if lives == 2:
        screen.blit(single_life_surf, pos_one_rect)
        screen.blit(single_life_surf, pos_two_rect)
        screen.blit(single_life_gray_surf, pos_three_gray_rect)
    if lives == 1:
        screen.blit(single_life_surf, pos_one_rect)
        screen.blit(single_life_gray_surf, pos_two_gray_rect)
        screen.blit(single_life_gray_surf, pos_three_gray_rect)
    if lives == 0:
        game_over_func()


def collision_sprite(score):
    if pygame.sprite.groupcollide(bullet_group, enemy_group, False, True):
        score += 1
    return score


def collision_ground():
    global lives
    if pygame.sprite.groupcollide(ground, enemy_group, False, True):
        lives -= 1


def game_over_func():
    global game_over
    game_over = True
    return


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                bullet_group.add(Bullet(screen, station.sprite.rot))
                alpha += 2
                enemy_speed += 0.02
                # increase_dificulty(alpha, enemy_speed)
                sky_red_surf.set_alpha(alpha)

            if event.type == obstacle_timer2:
                enemy_group.add(Enemy(screen))

    if game_active:
        if game_over == False:
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
            display_score(score, "Score: ", (300, 50))
        else:
            screen.blit(sky_surf, (0, 0))
            display_score(score, "", (300, 250))
            score_surf = test_font.render(
                f'Oh no, you lost.', False, (64, 64, 64))
            score_rect = score_surf.get_rect(center=(300, 175))
            screen.blit(score_surf, score_rect)
            score_surf = test_font.render(
                f'Here is your final score:', False, (64, 64, 64))
            score_rect = score_surf.get_rect(center=(300, 205))
            screen.blit(score_surf, score_rect)

    pygame.display.update()
    clock.tick(60)
