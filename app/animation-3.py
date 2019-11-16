import pygame,sys
pygame.init()
winwidth=500
winheigth=480
win=pygame.display.set_mode((winwidth,winheigth))
pygame.display.set_caption('my game')

clock = pygame.time.Clock()

x=y=50
width=40
heigth=60
vel=5

isJump=False
jumpCount=10

left =False
right=False
walkCount=0

walkRight = [pygame.image.load('images/R1.png'),\
			 pygame.image.load('images/R2.png'), \
			 pygame.image.load('images/R3.png'), \
			 pygame.image.load('images/R4.png'), \
			 pygame.image.load('images/R5.png'), \
			 pygame.image.load('images/R6.png'), \
			 pygame.image.load('images/R7.png'), \
			 pygame.image.load('images/R8.png'), \
			 pygame.image.load('images/R9.png')]

walkLeft = [pygame.image.load('images/L1.png'), \
			pygame.image.load('images/L2.png'), \
			pygame.image.load('images/L3.png'), \
			pygame.image.load('images/L4.png'), \
			pygame.image.load('images/L5.png'), \
			pygame.image.load('images/L6.png'), \
			pygame.image.load('images/L7.png'), \
			pygame.image.load('images/L8.png'), \
			pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')

def redrawGameWindow():
	global walkCount
	# This will draw our background image at (0,0)
	win.blit(bg,(0,0))
	if walkCount+1>=27:
		walkCount=0
	# if we facing left
	if left:
		# We integer divide walkCounr by 3 to ensure each
		# image is shown 3 times every animation
		win.blit(walkLeft[walkCount//3],(x,y))
		walkCount+=1
	elif right:
		win.blit(walkRight[walkCount//3],(x,y))
		walkCount+=1
	else:
		# if  the character is still standing
		win.blit(char,(x,y))
	pygame.display.update()

run=True
while run:
	clock.tick(27)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>vel:
		x-=vel
		left=True
		right=False

	elif keys[pygame.K_RIGHT] and x<winwidth-width:
		x+=vel
		left=False
		right=True

	else:
		# If the character is not moving 
		# we will set both left and right false and reset the animation counter (walkCount)
		left=False
		right=False
		walkCount


	if not isJump:
		if keys[pygame.K_UP] and y>vel:
			y-=vel
		elif keys[pygame.K_DOWN] and y<winheigth-heigth:
			y+=vel
		elif keys[pygame.K_SPACE]:
			isJump= not isJump
			right=False
			left=False
			walkCount=0

	else:
		#
		#if jumpCount>=-10:
		#	y-=jumpCount*abs(jumpCount)
		#	jumpCount-=1
	
		if jumpCount>=-10:
			neg=1
			if jumpCount<0:
				neg=-1
			y-=(jumpCount**2)*0.5*neg
			jumpCount-=1
		else:
			isJump=not isJump
			jumpCount=10

	redrawGameWindow()

pygame.quit()
sys.exit()
