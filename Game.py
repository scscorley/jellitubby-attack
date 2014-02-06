import pygame, sys, math, random

pygame.init()

from Monster import Monster
from Vacuum import Vacuum
from Bullet import Bullet
from HealthBar import HB
from Slow_Time import SlowTime
from heart import Heart
from nuke import Nuke
from pierce import Pierce
from PiercingBullet import PiercingBullet
from supervacuum import SuperVacuum
from superman import Superman
clock = pygame.time.Clock()


width = 1024
height = 652
size = width, height
killCount = 0
pause = False
nukeCount = 0

altFlag = False
fullscreen = 0

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("Resources/Background/start.png")
bgRect = bgImage.get_rect()

bgColor = r,g,b = 0,0,0

vacuum = Vacuum([3,3], [100,100], [width/2,height/2])
healthbar = HB(vacuum)
bullets = []
powerUps = []

font = pygame.font.Font(None, 36)

monsters = [Monster([random.randint(-5,5), random.randint(-5,5)], 
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
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                        altFlag = True
                if (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
                    
            if event.type == pygame.KEYUP:        
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False  
        
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.font.init()
    pygame.display.set_caption("Jellitubby Attack")
    

    level = 1
    bgImage = pygame.image.load("Resources/Background/newToilet5.png")
    bgRect = bgImage.get_rect()
    text = font.render("Level " + str(level), 1, (250, 250, 250))
    textpos = text.get_rect(centerx=screen.get_width()/2)

    
    piercing = False
    piercingTimer = 0
    piercingMaxTimer = 60 * 15
    
    supermode = False
    supermodeTimer = 0
    supermodeMaxTimer = 60 * 15
    
    
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
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                        altFlag = True
                if event.key == pygame.K_SPACE:
                    if nukeCount > 0:
                        nukeCount -= 1
                        for monster in monsters:
                            monster.living = False
                if (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
                if event.key == pygame.K_p:
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    pause = False
                                if (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and altFlag:
                                    if fullscreen == 0:
                                        fullscreen = pygame.FULLSCREEN
                                    else:
                                        fullscreen = 0
                                    screen = pygame.display.set_mode((width,height),fullscreen)
                                    pygame.display.flip()
                        
                        pauseFont = pygame.font.Font(None, 72)
                        pauseText = pauseFont.render("Paused", 1, (0,0,0))
                        pauseTextPos = pauseText.get_rect(centerx=width/2, centery=height/2)
                                    
                        screen.fill(bgColor)
                        screen.blit(bgImage, bgRect)
                        screen.blit(text, textpos)
                        for powerUp in powerUps:
                            screen.blit(powerUp.image, powerUp.rect)
                        for bullet in bullets:
                            screen.blit(bullet.image, bullet.rect)
                        screen.blit(vacuum.image, vacuum.rect)
                        screen.blit(healthbar.image, healthbar.rect)
                        for monster in monsters:
                            screen.blit(monster.image, monster.rect)
                        screen.blit(nukeText, nukeTextPos)
                        screen.blit(pauseText, pauseTextPos)
                        pygame.display.flip()
                        clock.tick(60)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    vacuum.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    vacuum.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    vacuum.direction("stop up")
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    vacuum.direction("stop down")
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                    altFlag = False
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if piercing:
                        bullets += [PiercingBullet(vacuum.rect.center, vacuum.angle)]
                    else:
                        bullets += [Bullet(vacuum.rect.center, vacuum.angle)]

          
                    
                
               
        if random.randint(0,1000) == 0:      #1 in 60 chance
            powerUps += [SlowTime([width/2, height/2+65])] 
        if random.randint(0,1000) == 0:
            powerUps += [Heart([width/2, height/2])]
        if random.randint(0,1000) == 0:
            powerUps += [Nuke([width/2, height/2+130])]
        if random.randint(0,1000) == 0:
            powerUps += [Pierce([width/2+65, height/2+65])]
        if random.randint(0,10) == 0:
            powerUps += [Superman([width/2-65, height/2+65])]
        
        for powerUp in powerUps:
            powerUp.update()
            if vacuum.collidePowerUp(powerUp):
                if powerUp.type == "slow time":
                    for monster in monsters:
                        monster.slowDown()
                if powerUp.type == "heart":
                    healthbar.heal()
                if powerUp.type == "nuke":
                    nukeCount += 1
                if powerUp.type == "pierce":
                    piercing = True
                    piercingTimer = piercingMaxTimer
                if powerUp.type == "superman":
                    supermode = True
                    supermodeTimer = supermodeMaxTimer
                    vacuum = SuperVacuum(vacuum.maxSpeed, [100,100], vacuum.rect.center)
            if not powerUp.living:
                powerUps.remove(powerUp)  
        
        if piercingTimer > 1:
            piercingTimer -= 1
        elif piercingTimer == 1:
            piercing = False
            piercingTimer -= 1
            
            
        if supermodeTimer > 1:
            supermodeTimer -= 1
        elif supermodeTimer == 1:
            supermode = False
            supermodeTimer -= 1
            vacuum = Vacuum(vacuum.maxSpeed, [100,100], vacuum.rect.center)
            
        

            
            
        for monster in monsters:
            monster.update()
            monster.collideWall(width, height)
            vacuum.collideMonster(monster)
            if not monster.living:
                monsters.remove(monster)
                killCount += 1
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
            text = font.render("Level " + str(level), 1, (250, 250, 250))
            textpos = text.get_rect(centerx=screen.get_width()/2)
            for i in range(level):
                monSize = [50, 50]
                onPlayer = True
                while onPlayer:
                    newMonster = Monster( 
                              [random.randint(-5,5), random.randint(-5,5)], 
                              [random.randint(75, width-75), random.randint(75, height-75)])
                    onPlayer = newMonster.collideVacuum(vacuum)
                monsters += [newMonster]
                
            
        nukeText = font.render("Nukes: " + str(nukeCount), 1, (250, 250, 250))
        nukeTextPos = nukeText.get_rect(centerx=280)
                              
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(text, textpos)
        for powerUp in powerUps:
            screen.blit(powerUp.image, powerUp.rect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        screen.blit(vacuum.image, vacuum.rect)
        screen.blit(healthbar.image, healthbar.rect)
        for monster in monsters:
            screen.blit(monster.image, monster.rect)
        screen.blit(nukeText, nukeTextPos)
        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
        #print level
       

    
    while start and not vacuum.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                    vacuum = Vacuum([3,3], [100,100], [width/2,height/2])
                    healthbar = HB(vacuum)
                    bullets = []
                    monsters = [Monster([random.randint(-5,5), random.randint(-5,5)], 
                                [random.randint(75, width-75), random.randint(75, height-75)])]
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                        altFlag = True
                if (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT) and altFlag:
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_RALT or event.key == pygame.K_LALT):
                   altFlag = False
        
        leaderFont = pygame.font.Font(None, 50)
        leaderTitle = leaderFont.render("Highscores", 1, (250, 250, 250))
        leaderTitlePos = leaderTitle.get_rect(centerx=screen.get_width()/2, centery=300)
        leaderFont = pygame.font.Font(None, 30)
        
        f = open("Resources/leaderboard.txt", "r")
        lines = f.readlines()
        f.close()
        
        
        
        leaderboard = []
        entryY = 360
        for line in lines:
            boardEntry = []
            leaderText = leaderFont.render(line, 1, (250, 250, 250))
            leaderTextPos = leaderText.get_rect(centerx=screen.get_width()/2, centery=entryY)
            entryY += 30
            boardEntry += [leaderText, leaderTextPos]
            leaderboard += [boardEntry]


        bgImage = pygame.image.load("Resources/Background/NewGameOver.png")
        bgRect = bgImage.get_rect()
        font = pygame.font.Font(None, 50)
        text = font.render("Jellies Killed: " + str(killCount), 1, (250, 0, 250))
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=230)  
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(text, textpos)
        screen.blit(leaderTitle, leaderTitlePos)
        for boardEntry in leaderboard:
            screen.blit(boardEntry[0], boardEntry[1])
        pygame.display.flip()

