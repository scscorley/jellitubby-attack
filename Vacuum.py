import pygame, sys, math

class Vacuum():
    def __init__(self, images, speed = [2,2], size = [100,100], pos = (0,0)):
        self.images = []
        for image in images:
            newimage = pygame.image.load(image)
            newimage = pygame.transform.scale(newimage, size)
            self.images += [newimage]
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.waitCount = 0
        self.waitMax = 10
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.didBounce = False
        self.health = 100
        mousePos = pygame.mouse.get_pos()
        angle = math.atan2(mousePos[1],mousePos[0])
        rot_image = pygame.transform.rotate(self.images[self.frame], angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image = rot_image
        self.living= True
        
    def place(self, pos):
        self.rect.center = pos
        
    def direction(self, dir):
        if dir == "right":
            self.speedx = self.maxSpeedx
        if dir == "stop right":
            self.speedx = 0
        if dir == "left":
            self.speedx = -self.maxSpeedx
        if dir == "stop left":
            self.speedx = 0
        if dir == "up":
            self.speedy = -self.maxSpeedy
        if dir == "stop up":
            self.speedy = 0
        if dir == "down":
            self.speedy = self.maxSpeedy
        if dir == "stop down":
            self.speedy = 0
    
    def update(self):
        self.move()
        self.animate()
        if self.health <= 0:
            self.living = False
        self.didBounce = False
        
    
    def animate(self):
        if self.waitCount < self.waitMax:
            self.waitCount += 1
        else:
            self.waitCount = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = 0
            self.didBounce = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = 0
            self.didBounce = True
            
    def collideBall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    if self.rect.center[0] < other.rect.center[0]: #self left of other
                        if other.speedx < 0: #moving left
                            if not other.didBounce:
                                other.speedx = -other.speedx
                                other.didBounce = True
                                self.health -= other.damage
                    if self.rect.center[0] > other.rect.center[0]: #self right of other
                        if other.speedx > 0: #moving right
                            if not other.didBounce:
                                other.speedx = -other.speedx
                                other.didBounce = True
                                self.health -= other.damage
                    if self.rect.center[1] < other.rect.center[1]: #self above other
                        if other.speedy < 0: #moving up
                            if not other.didBounce:
                                other.speedy = -other.speedy
                                other.didBounce = True
                                self.health -= other.damage
                    if self.rect.center[1] > other.rect.center[1]:#self below other
                        if other.speedy > 0: #moving down
                            if not other.didBounce:
                                other.speedy = -other.speedy
                                other.didBounce = True
                                self.health -= other.damage
                 
                    
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))