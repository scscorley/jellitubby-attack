import pygame, sys, math

from Bullet import Bullet

class PiercingBullet(Bullet):
    def __init__(self, pos, angle):
        Bullet.__init__(self, pos, angle)
        self.image = pygame.image.load("Resources/powerUps/pierce.png")
        self.rect = self.image.get_rect()
        self.angle = angle
        self.rot_angle = self.angle - 90
        rot_image = pygame.transform.rotate(self.image, self.rot_angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.place(pos)
        self.radius = self.rect.height/2
        
    
    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False
    