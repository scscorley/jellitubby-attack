import pygame, sys, math

class Bullet():
	
	
	def direction(self):
        pass
	
	def update(self):
        pass
	
	def move(self):
		self.speed = [self.speedx, self.speedy]
		self.rect = self.rect.move(self.speed)
		
	
	
	def collideBall(self, other):
		if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				if self.radius + other.radius > self.distanceToPoint(other.rect.center):
					other.living = False
					bullet.living = False
					
   
   def collideWall(self, width, height):
		if self.rect.left < 0 or self.rect.right > width:
			bullet.living = False
		if self.rect.top < 0 or self.rect.bottom > height:
			bullet.living = False
   
   
   def place(self, pos):
		self.rect.center = pos
        
   
   
   
   
	