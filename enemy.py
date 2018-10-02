import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, screen, enemy_x = 1, enemy_y = 1):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.x = enemy_x
        self.rect.y = enemy_y
        self.move_dir = 1
        self.drop = 5

    def get_num(self):
        # 根据screen宽度计算一行有多少个
        #(self.screen.width-2*self.rect.width）//(2*self.rect.width)
        return 6

    def get_row(self):
        # 根据screen高度计算有多少行
        # (self.screen.width)
        return 3

    def check_edge(self):
        if self.rect.left <= self.screen_rect.left:
            return True
        elif self.rect.right >= self.screen_rect.right:
            return True 

    def move_down(self):
        self.rect.y += self.drop

    def update(self):
        # print(self.rect.x)
        self.rect.left += self.move_dir
