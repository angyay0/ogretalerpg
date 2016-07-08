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

#principal
ancho,alto=500,400
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('Charas RPG')

gengar= chara_linea(80,80,'gg.png')
skarmory= chara_linea(80,80,'sk.png')
scizor= chara_linea(80,80,'sc.png')
absol= chara_linea(80,80,'ab.png')


reloj = pygame.time.Clock()
ttol=500
delta=0
frame=0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
#esta_es_la_animacion_
	if pygame.time.get_ticks()-delta>ttol:
		delta= pygame.time.get_ticks()	
		frame+=1
		if frame>1:
			frame=0
	
	
	pantalla.blit(gengar[frame],(45,45))
	pantalla.blit(skarmory[frame],(135,0))
	pantalla.blit(absol[frame],(200,250))	
	pantalla.blit(scizor[frame],(50,145))
	pygame.display.update()
	reloj.tick(30)













			
