import pygame
import sys

from pygame.locals import *

import math

pygame.init()


display_width = 800
display_height = 600
display = pygame.display.set_mode( (display_width, display_height) )
display_center_x = display_width / 2.0
display_center_y = display_height / 2.0

pygame.display.set_caption("Sub-project")


#colors
white =  (255, 255, 255)
black =  (0, 0 , 0)
red =    (255, 0 , 0)
green =  (0, 255, 0)
blue =   (0, 0, 255)
cyan =   (0, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)

UP    = "up"
DOWN  = "down"
RIGHT = "right"
LEFT  = "left"



def radians_to_degrees(radians):
	return (radians / math.pi) * 180.0

def degrees_to_radians(degrees):
	return degrees * (math.pi / 180.0)


GRAD = math.pi / 180

#single_pixel = pygame.PixelArray(display)
#single_pixel[3][3] = yellow


#display.fill(red)

#pygame.draw.line(display, green, (10,10), (100,100), 10)
#pygame.draw.circle(display, green, (300,300), 50,20)
#pygame.draw.rect(display, green, (300,300, 200, 50))
#pygame.draw.polygon(display, green, ( (100,100), (300,300), (500,100) ) )

ship_image = pygame.image.load("ship1.png")
ship_image = pygame.transform.scale(ship_image, (80,80))
ship_image_x = 10
ship_image_y = 10

bullet_image = pygame.image.load("bullet1.png")
bullet_image = pygame.transform.scale(bullet_image, (5,5))
bullet_image_x = 10
bullet_image_y = 10

background_image = pygame.image.load("level1.jpg").convert()


FPS = 30
fps_time = pygame.time.Clock()


def makeTextObjs(text, font, color):
	text_surface = font.render(text, True, color)
	return text_surface, text_surface.get_rect()


def whatNext():
	for event in pygame.event.get([QUIT, KEYUP, KEYDOWN]):
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYUP:
			continue
		return event.key
	return None


def msgSurface(text, text_color):
	small_text = pygame.font.Font("freesansbold.ttf", 20)
	large_text = pygame.font.Font("freesansbold.ttf", 150)

	title_text_surface, title_text_rect = makeTextObjs(text, large_text, text_color)
	title_text_rect.center = (int(400), int(300))
	display.blit(title_text_surface, title_text_rect)

	type_text_surface, type_text_rect = makeTextObjs("Press key to continue", small_text, text_color)
	type_text_rect = (int(400), int(400))
	display.blit(type_text_surface, type_text_rect)

	pygame.display.update()
	fps_time.tick()

	while whatNext() == None:
		for event in pygame.event.get([QUIT]):
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fps_time.tick()


mili = fps_time.tick(FPS)
playtime = 0.0

#xpos = pixelperx * seconds
#ypos = pixelpery * seconds

ship_image_original = ship_image.copy()
angle = 0
turnspeed = 180
turnfactor = 1
bullet_image_original = bullet_image.copy()
bullet_angle = 0


#display.blit(ship_image, (ship_image_x, ship_image_y))


viewport = background_image.subsurface(( (0,0), (12384, 2048) ))
display.blit(viewport, (0,0))

display_center_x = display_center_x - (ship_image.get_width() / 2.0)
display_center_y = display_center_y - (ship_image.get_height() / 2.0)

display.blit(ship_image, (display_center_x , display_center_y ))

fire = False
bullet_seconds = 0.0

while True:

	
	milliseconds = fps_time.tick(FPS)
	playtime += milliseconds / 1000.0
	seconds = milliseconds / 1000.0

	for event in pygame.event.get():
		#print event
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				pass
			elif event.key == K_RIGHT:
				pass
			elif event.key == K_UP:
				pass
			elif event.key == K_DOWN:
				pass
				#msgSurface("DEAD!", red)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		display.fill(black)
		ship_image_x += -math.sin(angle * GRAD) * turnspeed * seconds
		ship_image_y += -math.cos(angle * GRAD) * turnspeed * seconds
		#display.blit(ship_image, (ship_image_x, ship_image_y))
		display.blit(viewport, (-ship_image_x,-ship_image_y))
		display.blit(ship_image, (display_center_x, display_center_y))
		pygame.display.flip()
	if keys[pygame.K_LEFT]:
		display.fill(black)
		angle+= turnfactor * turnspeed * seconds
		oldrect = ship_image.get_rect()
		ship_image = pygame.transform.rotate(ship_image_original, angle)
		newrect = ship_image.get_rect()
		ship_image_x += oldrect.centerx - newrect.centerx
		ship_image_y += oldrect.centery - newrect.centery
		#display.blit(ship_image, (ship_image_x, ship_image_y))
		display.blit(viewport, (-ship_image_x,-ship_image_y))
		display.blit(ship_image, (display_center_x, display_center_y))
		pygame.display.flip()
	if keys[pygame.K_RIGHT]:
		display.fill(black)
		angle+= -turnfactor * turnspeed * seconds
		oldrect = ship_image.get_rect()
		ship_image = pygame.transform.rotate(ship_image_original, angle)
		newrect = ship_image.get_rect()
		ship_image_x += oldrect.centerx - newrect.centerx
		ship_image_y += oldrect.centery - newrect.centery
		#display.blit(ship_image, (ship_image_x, ship_image_y))
		display.blit(viewport, (-ship_image_x,-ship_image_y))
		display.blit(ship_image, (display_center_x, display_center_y))
		pygame.display.flip()
	if keys[pygame.K_DOWN]:
		display.fill(black)
		ship_image_x += +math.sin(angle * GRAD) * turnspeed * seconds
		ship_image_y += +math.cos(angle * GRAD) * turnspeed * seconds

		display.blit(viewport, (-ship_image_x,-ship_image_y))
		
		#display.blit(ship_image, (ship_image_x, ship_image_y))
		display.blit(ship_image, (display_center_x, display_center_y))
		pygame.display.flip()
	if keys[pygame.K_SPACE]:
		fire = True

		print bullet_image_x
		#bullet_image_x = ship_image_x + ship_image.get_width()/2.0
		bullet_image_x = display_center_x
		print bullet_image_x
		#bullet_image_x = ship_image.get_rect().centerx
		#bullet_image_y = ship_image_y + ship_image.get_height()/2.0
		bullet_image_y = display_center_y
		#bullet_image_y = ship_image_y
		#bullet_image_y = ship_image.get_rect().centery
		bullet_angle = angle
		display.blit(bullet_image, (bullet_image_x, bullet_image_y))
		old_bullet_rect = bullet_image.get_rect()
		#bullet_rot_angle = math.atan2(-bullet_image_x, -bullet_image_y) / math.pi * 180.0
		bullet_rot_angle = angle
		bullet_image = pygame.transform.rotate(bullet_image_original, bullet_rot_angle)
		new_bullet_rect = bullet_image.get_rect()
		
		#bullet_image_x += old_bullet_rect.centerx - new_bullet_rect.centerx
		bullet_image_x = display_center_x + (ship_image.get_width() / 2.0)
		#bullet_image_y += old_bullet_rect.centery - new_bullet_rect.centery
		bullet_image_y = display_center_y + (ship_image.get_height() / 2.0)

		display.blit(bullet_image, (bullet_image_x, bullet_image_y))
		pygame.display.flip()
		bullet_seconds = playtime

	if fire:
		display.fill(black)
		bullet_image_x += -math.sin(bullet_angle * GRAD) * turnspeed * seconds
		bullet_image_y += -math.cos(bullet_angle * GRAD) * turnspeed * seconds

		display.blit(viewport, (-ship_image_x,-ship_image_y))
		display.blit(bullet_image, (bullet_image_x, bullet_image_y))
		#display.blit(ship_image, (ship_image_x, ship_image_y))
		
		display.blit(ship_image, (display_center_x, display_center_y))
		pygame.display.flip()

		if playtime - bullet_seconds > 3.0:
			fire = False
			display.fill(black)
			#display.blit(ship_image, (ship_image_x, ship_image_y))
			display.blit(viewport, (-ship_image_x,-ship_image_y))
			display.blit(ship_image, (display_center_x, display_center_y))
			pygame.display.flip()

	text = "Sub project      FPS: {0:.2f}   Playtime: {1:.2f}     :D".format(fps_time.get_fps(), playtime)
	#print ship_image_x
	#print ship_image_y
	pygame.display.set_caption(text)
	pygame.display.update()
	#print playtime
	print display_center_x
	print display_center_y
