import pygame 
import random
import math

NEGRO = [0,0,0]
ANCHO = 640
ALTO = 480
VERDE = [0,255,0]
NEGRO = [0,0,0]
NARANJA = (255,120,9)
ROJO = (255,0,0)
AZUL = (0,0,255)
MORADO = (128,0,128)
AMARILLO = (255,255,0)
GRIS = (128,128,128)

class gato(pygame.sprite.Sprite):
	def __init__(self,mat_i,pos_ini):
		pygame.sprite.Sprite.__init__(self)
		self.m = mat_i
		self.col = 0
		self.dir = 2
		self.image = self.m[self.dir][self.col]
		self.rect = self.image.get_rect()
		self.rect.x = pos_ini[0]
		self.rect.y = pos_ini[1]
		self.velx = 0
		self.vely = 0
		self.vidas = 3

	def update(self):
		self.image = self.m[self.dir][self.col]
		if self.velx != 0 or self.vely != 0:
			if self.col < 2:
				self.col += 1
			else:
				self.col = 0
			self.rect.x += self.velx
			self.rect.y += self.vely
class raton(pygame.sprite.Sprite):
    '''
    clase rival
    '''
    def __init__(self,mat_i,pos_ini):
    	pygame.sprite.Sprite.__init__(self)
    	self.m = mat_i
    	self.col = 9
    	self.dir = 2
    	self.image = self.m[self.dir][self.col]
    	self.rect = self.image.get_rect()
    	self.rect.x = pos_ini[0]
    	self.rect.y = pos_ini[1]
    	self.velx = 0
    	self.vely = 0

	def update(self):
		self.image = self.m[self.dir][self.col]
		if self.velx != 0 or self.vely != 0:
			if self.col < 11:
				self.col += 1
			else:
				self.col = 9

				self.rect.x += self.velx
				self.rect.y += self.vely


def pendiente(puntoini,puntofin):
	num = puntofin[1]-puntoini[1]
	den = puntofin[0]-puntoini[0]
	if den == 0:
		m = 0
	else: 
		m = float(num/den)
		b = float(puntofin[1]-(m*puntofin[0]))

def matrizrecorte(ancho_corte,alto_corte,ancho_img,alto_img,img):
	matriz = []
	columnas = ancho_img/ancho_corte
	filas = alto_img/alto_corte
	for i in range(int(filas)):
		matriz.append([])
		for j in range(int(columnas)):
			matriz[i].append(img.subsurface(j*32,i*32,ancho_corte,alto_corte))
	return matriz	

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
	img = pygame.image.load('animales.png')
	info = img.get_rect()
	ancho_img = info[2]
	alto_img = info[3]

	print('ancho: ',ancho_img,'alto: ',alto_img)
	matriz = matrizrecorte(32,32,ancho_img,alto_img,img)
	gatos = pygame.sprite.Group()
	ratones = pygame.sprite.Group()
	g = gato(matriz,[100,120])
	gatos.add(g)


	#crear rivales
	n = 10

	for i in range(n):
		r = raton(matriz,[300,150])
		r.rect.x= random.randrange(ANCHO - r.rect.width)
		r.rect.y= random.randrange(ALTO - r.rect.height)
		ratones.add(r)
	fuente = pygame.font.Font(None,34)
	cad = 'vidas: '+ str(g.vidas)
	texto = fuente.render(cad,False,MORADO)
	ptos = 0
	reloj = pygame.time.Clock()
	fin_juego = False
	fin = False

	fin = False
	reloj = pygame.time.Clock()
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					g.dir = 1
					g.velx = -3
					g.vely = 0
				if event.key == pygame.K_RIGHT:
					g.dir = 2
					g.velx = 3
					g.vely = 0
				if event.key == pygame.K_UP:
					g.dir = 3
					g.velx = 0
					g.vely = -3
				if event.key == pygame.K_DOWN:
					g.dir = 0
					g.velx = 0
					g.vely = 3
			if event.type == pygame.KEYUP:
				g.velx = 0
				g.vely = 0
		for g in gatos:
			if g.rect.x > (ANCHO - g.rect.width):
				g.velx = -1
			if g.rect.x <= 0:
				g.velx = 1
			if g.rect.y > (ALTO - g.rect.width):
				g.vely = -1
			if g.rect.y <= 0:
				g.vely = 1

		pantalla.fill(NEGRO)
		gatos.update()
		ratones.update()
		ratones.draw(pantalla)
		gatos.draw(pantalla)
		pygame.display.flip()
		reloj.tick(25)