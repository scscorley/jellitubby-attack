import pygame, sys, math

class Monster():
    def __init__(self, image, speed = [2,2], size = [100,100], pos = (0,0)):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.didBounce = False
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        self.move()
        self.didBounce = False
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    if self.rect.center[0] < other.rect.center[0]: #self left of other
                        if self.speedx > 0: #moving right
                            if not self.didBounce:
                                self.speedx = -self.speedx
                                self.didBounce = True
                        if other.speedx < 0: #moving left
                            if not self.didBounce:
                                other.speedx = -other.speedx
                                self.didBounce = True
                    if self.rect.center[0] > other.rect.center[0]: #self right of other
                        if self.speedx < 0: #moving left
                            if not self.didBounce:
                                self.speedx = -self.speedx
                                self.didBounce = True
                        if other.speedx > 0: #moving right
                            if not self.didBounce:
                                other.speedx = -other.speedx
                                self.didBounce = True
                    if self.rect.center[1] < other.rect.center[1]: #self above other
                        if self.speedy > 0: #moving down
                            if not self.didBounce:
                                self.speedy = -self.speedy
                                self.didBounce = True
                        if other.speedy < 0: #moving up
                            if not self.didBounce:
                                other.speedy = -other.speedy
                                self.didBounce = True
                    if self.rect.center[1] > other.rect.center[1]:#self below other
                        if self.speedy < 0: #moving up
                            if not self.didBounce:
                                self.speedy = -self.speedy
                                self.didBounce = True
                        if other.speedy > 0: #moving down
                            if not self.didBounce:
                                other.speedy = -other.speedy
                                self.didBounce = True
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))