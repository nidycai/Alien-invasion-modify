import sys

import pygame
from game_settings import GameSettings
from ship import Ship


class Game():
    def __init__(self, settings):
        self.settings = settings
        pygame.init()
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Alien Invasion')
        

    def run(self):
        self.ship = Ship(self.screen_rect)
        self.screen.fill(self.settings.bg_color) 


        print('游戏开始')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.move(-self.settings.speed)
                    if event.key == pygame.K_RIGHT:
                        self.ship.move(self.settings.speed)
                    if event.key == pygame.K_SPACE:
                        self.ship.fire()
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()



settings = GameSettings()
game = Game(settings)
game.run()