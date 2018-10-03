import sys

import pygame
from game_settings import GameSettings
from ship import Ship

import game_function as gf


class Game():
    def __init__(self):
        self.settings = GameSettings()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Alien Invasion')
        

    def run(self):
        self.ship = Ship(self.screen)
        enemy_fleet = pygame.sprite.Group()
        gf.create_fleet(self.screen, enemy_fleet)
        print('游戏开始')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_SPACE:
                        self.ship.fire()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
            # if len(enemy_fleet) == 0:
            #     enemy_fleet = gf.create_fleet(self.screen)
            self.screen.fill(self.settings.bg_color)
            # gf.check_collison(enemy_fleet, self.ship.bullets)
            gf.check_collide(enemy_fleet, self.ship.bullets, self.ship, self.screen)
            gf.update_enemy(enemy_fleet)
            # enemy_fleet.update()
            enemy_fleet.draw(self.screen)
            self.ship.update()
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()



game = Game()
game.run()