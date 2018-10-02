import sys

import pygame
from game_settings import GameSettings
from ship import Ship
import game_function as gf


class Game():
    def __init__(self, settings):
        self.settings = settings
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Alien Invasion')
        

    def run(self):
        self.ship = Ship(self.screen)

        print('游戏开始')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.settings.speed = -1
                    if event.key == pygame.K_RIGHT:
                        self.settings.speed = 1
                    if event.key == pygame.K_SPACE:
                        self.ship.fire()
                if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
                    self.settings.speed = 0

            self.screen.fill(self.settings.bg_color)
            enemy_fleet = gf.create_fleet(self.screen)
            # gf.update_enemy(enemy_fleet)
            enemy_fleet.update()
            enemy_fleet.draw(self.screen)
            self.ship.update(self.settings.speed)
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()



settings = GameSettings()
game = Game(settings)
game.run()