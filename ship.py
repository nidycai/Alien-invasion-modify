import pygame
from bullets import Bullets 

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 
        self.bullets = pygame.sprite.Group() 
    
    def move(self, direction):
        if self.rect.left>0 and self.rect.right<self.screen_rect.right:
            self.rect.x += direction 


    def fire(self):
        if len(self.bullets) < 3:
            self.bullets.add(Bullets(self.rect))

    def update(self, direction):
        self.move(direction)
        bullet_remove = []
        for bullet in self.bullets:
            if bullet.check_edge():
                bullet_remove.append(bullet)
        for bullet in bullet_remove:
            self.bullets.remove(bullet)
        for bullet in self.bullets:
            bullet.draw_bullet(self.screen)
