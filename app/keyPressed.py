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
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] :
		x-=vel
	elif keys[pygame.K_RIGHT]:
		x+=vel
	elif keys[pygame.K_UP]:
		y-=vel
	elif keys[pygame.K_DOWN]:
		y+=vel
	win.fill((0,0,0))
	pygame.draw.rect(win,(255,0,0),(x,y,width,heigth))
	pygame.display.update()
pygame.quit()
sys.exit()
