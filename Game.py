import pygame, sys, math, random

pygame.init()

from Monster import Monster
from Vacuum import Vacuum
from Bullet import Bullet
from HealthBar import HB
from Slow_Time import SlowTime
clock = pygame.time.Clock()


#pygame.mixer.music.load('Resources\Sounds\Music\monster.mp3')
#pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
#pygame.mixer.music.play(-1)

width = 1100
height = 700
size = width, height
KILLS = 0


screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Resources/Background/start.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0


#FUCKTHEPOLICE


vacuum = Vacuum(["Resources/Player/Vacuum.png"], [3,3], [100,100], [width/2,height/2])
healthbar = HB(vacuum)
bullets = []
powerUps = []


monsters = [Monster([random.randint(-5,5), random.randint(-5,5)], 
			  [random.randint(75, width-75), random.randint(75, height-75)])]
			  
start = False
while True:
              
start = True
while True:
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
        
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
        
    level = 1
    bgImage = pygame.image.load("Resources/Background/TOILET1.png")
    bgRect = bgImage.get_rect()
    
    while start and vacuum.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    vacuum.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    vacuum.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    vacuum.direction("up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    vacuum.direction("down")
                
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    vacuum.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    vacuum.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    vacuum.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    vacuum.direction("stop down")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets += [Bullet(vacuum.rect.center, vacuum.angle)]
               
        if random.randint(0,10000) == 0:      #1 in 60 chance
            powerUps += [SlowTime([width/2+20, height/2+65])]
        for powerUp in powerUps:
            powerUp.update()
            if vacuum.collidePowerUp(powerUp):
                if powerUp.type == "slow time":
                    for monster in monsters:
                        monster.slowDown()
            if not powerUp.living:
                powerUps.remove(powerUp)
        
        for monster in monsters:
            monster.update()
            monster.collideWall(width, height)
            vacuum.collideMonster(monster)
            if not monster.living:
                monsters.remove(monster)
        if len(monsters) > 1:
            for first in range(len(monsters)-1):
                for second in range(first+1,len(monsters)):
                    monsters[first].collideMonster(monsters[second])
            
        for bullet in bullets:
            bullet.update()
            bullet.collideWall(width,height)
            for monster in monsters:
                bullet.collideMonster(monster)
            if not bullet.living:
                bullets.remove(bullet)
                
        vacuum.update() 
        vacuum.collideWall(width, height)
        
        healthbar.update()
        
        if len(monsters) == 0:
            level += 1
            for i in range(level):
                monSize = [50, 50]
                monsters += [Monster( 
                              [random.randint(-5,5), random.randint(-5,5)], 
                               
                              [random.randint(75, width-75), random.randint(75, height-75)])]
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for powerUp in powerUps:
            screen.blit(powerUp.image, powerUp.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        screen.blit(vacuum.image, vacuum.rect)
        screen.blit(healthbar.image, healthbar.rect)
        for monster in monsters:
            screen.blit(monster.image, monster.rect)
        pygame.display.flip()
        clock.tick(60)
        #print level

    
    bgImage = pygame.image.load("Resources/Background/GameOver.png")
    bgRect = bgImage.get_rect() 
    
    while start and not vacuum.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                    vacuum = Vacuum(["Resources/Player/Vacuum.png"], [3,3], [100,100], [width/2,height/2])
                    healthbar = HB(vacuum)
                    bullets = []
                    monsters = [Monster([random.randint(-5,5), random.randint(-5,5)], 
                                [random.randint(75, width-75), random.randint(75, height-75)])]
                    
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for powerUp in powerUps:
            screen.blit(powerUp.image, powerUp.rect)
        pygame.display.flip()
