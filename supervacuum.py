import pygame, sys, math

from Vacuum import Vacuum

class SuperVacuum(Vacuum):
    def __init__(self, speed = [2,2], size = [100,100], pos = (0,0)):
        Vacuum.__init__(self, speed, size, pos)
        self.baseImage = pygame.image.load("Resources/Player/superVacuum.png")
        self.baseImage = pygame.transform.scale(self.baseImage, size)
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
     
    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False
                    