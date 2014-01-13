import pygame, sys, math

class SlowTime():
    def __init__(self, pos = (0,0)):
        self.type = "slow time"
        self.image = pygame.image.load("Resources/powerUps/Slow_Time.png")
        self.image = pygame.transform.scale(self.image, [50,50])
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.timer = 60*7
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.living = False