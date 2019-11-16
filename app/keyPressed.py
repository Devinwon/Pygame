import pygame,sys
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('my game')
x=y=50
width=40
heigth=60
vel=5
run=True
while run:
	# This will delay the game the given amount of milliseconds. 
	# In our casee 0.1 seconds will be the delay
	pygame.time.delay(100)

	# This will loop through a list of any keyboard or mouse events.
	for event in pygame.event.get():
		# Checks if the red(close) button in the corner(on the top right) of the window is clicked
		if event.type==pygame.QUIT:
			run=False

	# This will give us a dictonary where each key has a value of 1 or 0. 
	# Where 1 is pressed and 0 is not pressed.			
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] :
		x-=vel
	elif keys[pygame.K_RIGHT]:
		x+=vel
	elif keys[pygame.K_UP]:
		y-=vel
	elif keys[pygame.K_DOWN]:
		y+=vel

	# draw over the previous shape before redrawing another one.	
	# Fills the screen with black
	win.fill((0,0,0))

	#This takes: window/surface, color, rect 
	pygame.draw.rect(win,(255,0,0),(x,y,width,heigth))

	# This updates the screen so we can see our rectangle
	pygame.display.update()
pygame.quit()
sys.exit()
