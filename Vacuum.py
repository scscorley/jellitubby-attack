import pygame, sys, math

class Vacuum():
    def __init__(self, image, speed = [2,2], size = [100,100], pos = (0,0)):
        self.baseImage = pygame.image.load("Resources/Player/Vacuum.png")
        self.baseImage = pygame.transform.scale(self.baseImage, size)
        self.rect = self.baseImage.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.didBounce = False
        self.health = 100
        self.maxHealth = 100
        mousePos = pygame.mouse.get_pos()
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.living= True
        self.invincible = False
        self.invincibleTimerMax = 30
        self.invincibleTimer = self.invincibleTimerMax

        
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
        
        if self.health <= 0:
            self.living = False
        
        if self.invincible:
           
            if self.invincibleTimer > 0:
                self.invincibleTimer -= 1
            else:
                self.invincible = False
                self.invincibleTimer = self.invincibleTimerMax
        
        mousePos = pygame.mouse.get_pos()
        mousePosPlayerX = mousePos[0] - self.rect.center[0]
        mousePosPlayerY = mousePos[1] - self.rect.center[1]
        self.angle = ((math.atan2(mousePosPlayerY, mousePosPlayerX))/math.pi)*180
        self.angle = -self.angle
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        self.didBounce = False
        
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
    

    def collideMonster(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    if not self.invincible:
                        self.health -= other.damage
                        self.invincible = True
                    
                    if self.rect.center[0] < other.rect.center[0]: #self left of other
                        if other.speedx < 0: #moving left
                            if not other.didBounce:
                                other.speedx = -other.speedx
                                other.didBounce = True
                    if self.rect.center[0] > other.rect.center[0]: #self right of other
                        if other.speedx > 0: #moving right
                            if not other.didBounce:
                                other.speedx = -other.speedx
                                other.didBounce = True
                    if self.rect.center[1] < other.rect.center[1]: #self above other
                        if other.speedy < 0: #moving up
                            if not other.didBounce:
                                other.speedy = -other.speedy
                                other.didBounce = True
                    if self.rect.center[1] > other.rect.center[1]:#self below other
                        if other.speedy > 0: #moving down
                            if not other.didBounce:
                                other.speedy = -other.speedy
                                other.didBounce = True
    def collidePowerUp(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False
                    return True
        return False
                 
                    
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))