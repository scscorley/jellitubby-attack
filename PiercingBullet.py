import pygame, sys, math

from Bullet import Bullet

class PiercingBullet(Bullet):
    def __init__(self, pos, angle):
        Bullet.__init__(self, pos, angle)
        self.timeMax = 60*10
    
    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False