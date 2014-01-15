import pygame, sys, math, random

class Monster():
    def __init__(self, speed = [2,2], pos = (0,0)):
        imgs = ["Resources/Monster/Blue.png",
                    "Resources/Monster/Blue2.png",
                    "Resources/Monster/Green.png",
                    "Resources/Monster/Orange.png",
                    "Resources/Monster/Pink.png",
                    "Resources/Monster/Yellow.png"]
        self.image = pygame.image.load(imgs[random.randint(0, len(imgs)-1)])
        self.rect = self.image.get_rect()
        w = self.rect.width
        h = self.rect.height
        self.image = pygame.transform.scale(self.image,[int(w * .25), int(h * .25)])
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.slowSpeedx = int(self.speedx/3)
        self.slowSpeedy = int(self.speedy/3)
        self.normalSpeedx = speed[0]
        self.normalSpeedy = speed[1]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        self.didBounce = False
        self.damage = 10
        self.slowTimeMax = 60*10
        self.slowTimer = self.slowTimeMax
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        self.move()
        self.didBounce = False
        if self.slowTimer < self.slowTimeMax:
            if self.slowTimer > 0:
                self.slowTimer -= 1
            else:
                self.slowTimer = self.slowTimeMax
                self.speedx = self.normalSpeedx
                self.speedy = self.normalSpeedy
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def slowDown(self):
        self.slowTimer = self.slowTimeMax-1
        self.speedx = self.slowSpeedx
        self.speedy = self.slowSpeedy
            
        
    def collideWall(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            if not self.didBounce:
                self.speedx = -self.speedx
                self.didBounce = True
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounce:
                self.speedy = -self.speedy
                self.didBounce = True
        if self.rect.center[0] < 0 or self.rect.center[0] > width:
            self.living = False
        if self.rect.center[1] < 0 or self.rect.center[1] > height:
            self.living = False
            
    def collideMonster(self, other):
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
                                
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    monster.living = False
                        
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))