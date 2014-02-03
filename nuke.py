import pygame, sys, math

class Nuke():
    def __init__(self, pos = (0,0)):
        self.type = "nuke"
        self.image = pygame.image.load("Resources/powerUps/smallNuke.png")
        self.image = pygame.transform.scale(self.image, [75,37])
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.timer = 60*10
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.living = False