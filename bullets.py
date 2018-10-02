import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, ship_rect):
        super().__init__()

        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.bottom = ship_rect.top
        self.rect.centerx = ship_rect.centerx
        self.color = ((0, 0, 0))    

    def update(self):
        self.rect.y -= 3

    def draw_bullet(self, screen):
        self.update()
        pygame.draw.rect(screen, self.color, self.rect)

    def check_edge(self):
        if self.rect.bottom < 0:
            return True 