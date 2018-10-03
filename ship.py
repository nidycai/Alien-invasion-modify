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
        self.moving_left, self.moving_right = 0, 0
    
    def move(self):
        if self.rect.left > self.screen_rect.left and self.moving_left:
            self.rect.left -= 1        
        if self.rect.right < self.screen_rect.right and self.moving_right:
            self.rect.centerx += 1 


    def fire(self):
        if len(self.bullets) < 3:
            self.bullets.add(Bullets(self.rect))

    def update(self):
        self.move()
        bullet_remove = []
        for bullet in self.bullets:
            if bullet.check_edge():
                bullet_remove.append(bullet)
        for bullet in bullet_remove:
            self.bullets.remove(bullet)
        for bullet in self.bullets:
            bullet.draw_bullet(self.screen)
