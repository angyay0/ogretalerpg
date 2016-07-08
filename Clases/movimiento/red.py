import pygame,sys
import time
from pygame import *


pygame.init()
#medoto_una_imagen_por_Seccion
#de_movimiento_chara
def chara_linea(xa,ya, nombre):
    anime = []
    base = pygame.image.load(nombre).convert_alpha()
    base_x, base_y = base.get_size()
    for i in range(int(base_x / xa)):
        anime.append(base.subsurface((i * xa, 0, xa, ya)))
    return anime

#medotodo_en_una_sola_imagen_todas_las_charas
def chara_cubo(xa,ya,nombre):
    anime = []
    base = pygame.image.load(nombre).convert_alpha()
    base_x, base_y = base.get_size()

    for j in range(int(base_y / ya)):
	  for i in range(int(base_x / xa)):
       		anime.append(base.subsurface((i * xa, j * ya , xa, ya)))
    return anime


	
#cosntructor
ancho,alto=500,400
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('Charas RPG')


red= chara_cubo(32,48,'red.png')
red_down=[red[0],red[1],red[2],red[3]]
red_izq=[red[4],red[5],red[6],red[7]]
red_drc=[red[8],red[9],red[10],red[11]]
red_up=[red[12],red[13],red[14],red[15]]

erik=red_down[0]
reloj = pygame.time.Clock()
x,y=23,14
dx,dy=4,4
db=100
delta=0
frame=0

while True:
	pantalla.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
	#tecla = pygame.key.get_pressed()
	if event.type == KEYDOWN:
		if event.key == K_y:
			red= chara_cubo(64,64,'onbike.png')
			red_down=[red[0],red[1],red[2],red[3]]
			red_izq=[red[4],red[5],red[6],red[7]]
			red_drc=[red[8],red[9],red[10],red[11]]
			red_up=[red[12],red[13],red[14],red[15]]	
			erik=red_down[0]	
			dx,dy=12,12		
		if event.key == K_UP:
			if (y-1)<0:
				y=alto
			else:
				y-=dy
				if pygame.time.get_ticks()-delta>db:
					delta= pygame.time.get_ticks()	
					frame+=1
					if frame>3:
						frame=0
				erik=red_up[frame]
		if event.key == K_DOWN:
			if y>=alto:
				y=0
			else:
				y+=dy
				if pygame.time.get_ticks()-delta>db:
					delta= pygame.time.get_ticks()	
					frame+=1
					if frame>3:
						frame=0
				erik=red_down[frame]
		if event.key == K_RIGHT:
			if x>=ancho:
				x=0
			else:
				x+=dx
				if pygame.time.get_ticks()-delta>db:
					delta= pygame.time.get_ticks()	
					frame+=1
					if frame>3:
						frame=0
				erik=red_drc[frame]
		if event.key == K_LEFT:
			if (x-1)<0:
				x=ancho
			else:
				x-=dx
				if pygame.time.get_ticks()-delta>db:
					delta= pygame.time.get_ticks()	
					frame+=1
					if frame>3:
						frame=0
				erik=red_izq[frame]							
		if event.key == K_t:
			red= chara_cubo(32,48,'red.png')
			red_down=[red[0],red[1],red[2],red[3]]
			red_izq=[red[4],red[5],red[6],red[7]]
			red_drc=[red[8],red[9],red[10],red[11]]
			red_up=[red[12],red[13],red[14],red[15]]	
			erik=red_down[0]			
			dx,dy=4,4

	pantalla.blit(erik,(x,y))
	pygame.display.update()
	reloj.tick(30)













			
