import pygame

class ScoreBoard():
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.life = 3
        self.stage = 1
    

    def level_up(self):
        self.stage += 1
    
    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score 