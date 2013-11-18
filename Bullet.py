import pygame, sys, math

class Bullet():
	
	
	def direction():
	
	
	def update():
	
	
	def move():
		self.speed = [self.speedx, self.speedy]
		self.rect = self.rect.move(self.speed)
		
	
	
	def collideBall():
		if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
			if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
				if self.radius + other.radius > self.distanceToPoint(other.rect.center):
					other.living = False
					bullet.living = False
					if self.rect.center[0] < other.rect.center[0]: #self left of other
						if other.speedx < 0: #moving left
							other.speedx = -other.speedx
					if self.rect.center[0] > other.rect.center[0]: #self right of other
						if other.speedx > 0: #moving right
							other.speedx = -other.speedx
					if self.rect.center[1] < other.rect.center[1]: #self above other
						if other.speedy < 0: #moving up
							other.speedy = -other.speedy
					if self.rect.center[1] > other.rect.center[1]:#self below other
						if other.speedy > 0: #moving down
							other.speedy = -other.speedy
   
   def collideWall():
		if self.rect.left < 0 or self.rect.right > width:
			bullet.living = False
		if self.rect.top < 0 or self.rect.bottom > height:
			bullet.living = False
   
   
   def place():
		bulletlist =[bullet(speed, player.rect.center)] 
   
   
   
   
	