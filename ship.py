import pygame
from bullets import Bullets

class Ship():
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom 
    
    def move(self, direction):
        if self.rect.left>0 and self.rect.right<self.screen_rect.right:
            self.rect.x += direction 


    def fire(self):
