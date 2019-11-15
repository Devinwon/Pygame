import pygame,sys
pygame.init()
winwidth=500
winheigth=400
win=pygame.display.set_mode((winwidth,winheigth))
pygame.display.set_caption('my game')
x=y=50
width=40
heigth=60
vel=5
run=True
isJump=False
jumpCount=10
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and x>vel:
		x-=vel
	elif keys[pygame.K_RIGHT] and x<winwidth-width:
		x+=vel
	if not isJump:
		if keys[pygame.K_UP] and y>vel:
			y-=vel
		elif keys[pygame.K_DOWN] and y<winheigth-heigth:
			y+=vel
		elif keys[pygame.K_SPACE]:
			isJump= not isJump
	else:
		if jumpCount>=-10:
			neg=1
			if jumpCount<0:
				neg=-1
			y-=(jumpCount**2)*0.5*neg
			jumpCount-=1
		else:
			isJump=not isJump
			jumpCount=10
	win.fill((0,0,0))
	pygame.draw.rect(win,(255,0,0),(x,y,width,heigth))
	pygame.display.update()
pygame.quit()
sys.exit()
