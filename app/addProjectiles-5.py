import pygame,sys
pygame.init()
winwidth=500
winheight=480
win=pygame.display.set_mode((winwidth,winheight))
pygame.display.set_caption('my game')

clock = pygame.time.Clock()

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

class projectile(object):
	def __init__(self,x,y,radius,color,facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing

	def draw(self,win):
		pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class player(object):
	def __init__(self,x,y,width,height):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.vel=5
		self.isJump=False
		self.left=False
		self.right=False
		self.walkCount=0
		self.jumpCount=10
		self.standing=True

	def draw(self,win):
		if self.walkCount+1>=27:
			self.walkCount=0

		if not self.standing:
			if self.left:
				win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
				self.walkCount+=1
			elif self.right:
				win.blit(walkRight[self.walkCount//3], (self.x,self.y))
				self.walkCount+=1
		else:
			if self.right:
				win.blit(walkRight[0],(self.x,self.y))
			else:
				win.blit(walkLeft[0],(self.x,self.y))

def redrawGameWindow():
	# This will draw our background image at (0,0)
	win.blit(bg,(0,0))
	man.draw(win)
	pygame.display.update()

run=True
man=player(200,410,64,64)
bullets = []
while run:
	clock.tick(27)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

	for bullet in bullets:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys=pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		if man.left:
			facing = -1
		else:
			facing = 1
			
		if len(bullets) < 5:
			bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

	if keys[pygame.K_LEFT] and man.x>man.vel:
		man.x-=man.vel
		man.left=True
		man.right=False
		man.standing=False
	elif keys[pygame.K_RIGHT] and man.x<winwidth-man.width:
		man.x+=man.vel
		man.left=False
		man.right=True
		man.standing=False
	else:
		# If the character is not moving 
		# we will set both left and right false and reset the animation counter (walkCount)
		man.standing=False
		man.walkCount=0


	if not man.isJump:
		if keys[pygame.K_UP] and man.y>man.vel:
			man.y-=man.vel
		elif keys[pygame.K_DOWN] and man.y<winheight-man.height:
			man.y+=man.vel
		elif keys[pygame.K_SPACE]:
			man.isJump= not man.isJump
			man.right=False
			man.left=False
			man.walkCount=0

	else:
		if man.jumpCount>=-10:
			neg=1
			if man.jumpCount<0:
				neg=-1
			man.y-=(man.jumpCount**2)*0.5*neg
			man.jumpCount-=1
		else:
			man.isJump=not man.isJump
			man.jumpCount=10

	redrawGameWindow()

pygame.quit()
sys.exit()
