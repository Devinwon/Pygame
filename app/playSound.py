import pygame,sys
from pygame.locals import *
import time 


pygame.init()
DISPLAYSURF=pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello world")

# soundObj = pygame.mixer.Sound('ringout.wav') 
# soundObj.play() 
# time.sleep(3) # wait and let the sound play for 1 second 
# soundObj.stop()

# Loading and playing background music: 
pygame.mixer.music.load('LongestNight.mp3')
pygame.mixer.music.play(-1, 0.0) 
# ...some more of your code goes here... 
time.sleep(20)
pygame.mixer.music.stop() 

while True:  #main in loop

	for event in pygame.event.get():
		if event.type==	QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

