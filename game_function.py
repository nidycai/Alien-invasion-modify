import pygame
from enemy import Enemy
from pygame.sprite import Group


def create_fleet(screen):
    enemies = Group()
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    enemy_width = enemy.rect.width
    nums = enemy.get_num()
    rows = enemy.get_row()

    for num in range(0, nums-1):
        for row in range(0, rows-1):
            create_enemy = Enemy(screen, enemy_width+2*enemy_width*num, enemy_height+2*enemy_height*row)
            enemies.add(create_enemy)
    return enemies

def update_enemy(enemies):
    drop = 0
    for enemy in enemies.sprites():
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


def check_alien_none(screen, enemies):
    if len(enemies) == 0:
        return create_fleet(screen)
            

        