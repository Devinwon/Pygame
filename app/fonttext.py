import pygame,sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello world")

WHITE = (255, 255, 255) 
GREEN = (  0, 255,   0) 
BLUE  = (  0,   0, 255) 

fontObj = pygame.font.Font('freesansbold.ttf', 32) 
textSurfaceObj = fontObj.render('Hello world!', True, GREEN) 
# textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE) 
textRectObj = textSurfaceObj.get_rect() 
textRectObj.center = (200, 150) 

while True:  #main in loop
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj) 
	for event in pygame.event.get():
		if event.type==	QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()