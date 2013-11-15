import pygame, sys, math, random

pygame.init()

from Monster import Monster
from Vacuum import Vacuum

clock = pygame.time.Clock()

width = 640
height = 480
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0,0,0

vacuum = Vacuum(["Resources/Player/Vacuum.png"], [3,3], [50,50], [width/2,height/2])

monSize = [50, 50]
monsters = [monster("Resources/Monster/Blue.png",
                    "Resources/Monster/Blue2.png",
                    "Resources/Monster/Green.png",
                    "Resources/Monster/Orange.png",
                    "Resources/Monster/Pink.png",
                    "Resources/Monster/Yellow.png",
              [random.randint(-5,5), random.randint(-5,5)], 
              [monSize, monSize], 
              [random.randint(75, width-75), random.randint(75, height-75)])]
              
start = False
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
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ballp.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ballp.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    ballp.direction("up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    ballp.direction("down")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    ballp.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    ballp.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    ballp.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    ballp.direction("stop down")

        for monster in monsters:
            monster.update()
        vacuum.update()        
        
        for monster in monsters:
            monster.collideWall(width, height)
        vacuum.collideWall(width, height)
        
        if len(monsters) > 1:
            for first in range(len(monsters)-1):
                for second in range(first+1,len(monsters)):
                    monsters[first].collideBall(monsters[second])
        
        for monster in monsters:
            vacuum.collideBall(monster)
            
        for monster in monsters:
            if not monster.living:
                monsters.remove(monster)
                
        
        if len(monsters) == 0:
            level += 1
            for i in range(level):
                print i
                monSize = [50, 50]
                monsters += [Monster("Resources/Monster/Blue.png", 
                              [random.randint(-5,5), random.randint(-5,5)], 
                              [monSize, monSize], 
                              [random.randint(75, width-75), random.randint(75, height-75)])]
                          
        screen.blit(bgImage, bgRect)
        screen.blit(vacuum.image, vacuum.rect)
        for monster in monsters:
            screen.blit(monster.image, monster.rect)
        pygame.display.flip()
        clock.tick(60)