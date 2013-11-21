import pygame, sys, math, random

pygame.init()

from Monster import Monster
from Vacuum import Vacuum
from Bullet import Bullet

clock = pygame.time.Clock()

width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0,0,0

bgImage = pygame.image.load("Resources/Background/background.png")
bgRect = bgImage.get_rect()

vacuum = Vacuum(["Resources/Player/Vacuum.png"], [3,3], [50,50], [width/2,height/2])
bullets = []

monsters = [Monster([random.randint(-5,5), random.randint(-5,5)], 
			  [random.randint(75, width-75), random.randint(75, height-75)])]
			  
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
	
	while start:
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
					bullets += [Bullet()]

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
		
		for bullet in bullets:
			bullet.update()
				
		
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
		screen.blit(bullet.image, bullet.rect)
		for monster in monsters:
			screen.blit(monster.image, monster.rect)
		pygame.display.flip()
		clock.tick(60)
