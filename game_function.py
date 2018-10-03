import pygame
from enemy import Enemy
from pygame.sprite import Group
from time import sleep

def create_fleet(screen, enemies):
    enemies.empty()
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    enemy_width = enemy.rect.width
    nums = enemy.get_num()
    rows = enemy.get_row()
    for num in range(0, nums-1):
        for row in range(0, rows-1):
            create_enemy = Enemy(screen, enemy_width+2*enemy_width*num, enemy_height+2*enemy_height*row)
            enemies.add(create_enemy)

def update_enemy(enemies):
    drop = 0
    for enemy in enemies:
        # print("111111111")
        if enemy.check_edge():
            drop = 1
            break
    if drop == 1:
        for enemy in enemies.sprites():
            enemy.move_down()
            enemy.move_dir *= -1
    enemies.update()
    
def check_collison(enemies, bullets):
    collision = pygame.sprite.groupcollide(enemies,bullets,True,True)


def check_bottom(enemies):
    for enemy in enemies:
        if enemy.check_bottom():
            return True
    return False


def check_ship_hit(enemies, ship):
    return pygame.sprite.spritecollideany(ship, enemies)

def check_collide(enemies, bullets, ship, screen):
    check_collison(enemies, bullets)
    if len(enemies)==0 or check_bottom(enemies) or check_ship_hit(enemies, ship):
        reset(ship, enemies, screen)
    #     create_fleet(screen, enemies)
    
    # if check_bottom(enemies):
    #     enemies.empty()
    #     create_fleet(screen, enemies)

    # if check_ship_hit(enemies, ship):
    #     sleep(0.5)
    #     create_fleet(screen, enemies)
    #     ship.centered()

def check_alien_none(screen, enemies):
    if len(enemies) == 0:
        create_fleet(screen, enemies)
            
def reset(ship, enemies, screen):
    if len(enemies) != 0:
        sleep(0.5)
        ship.centered()
    enemies.empty()
    create_fleet(screen, enemies)


        