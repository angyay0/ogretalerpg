import pygame
from pygame.locals import *

#controles
class Evento:
	#Control_Teclado_teclas_pulsadas_
	def teclado(self,event,tecla):
		#Control_tecla_pulsada
		if event.type == KEYDOWN:
			#Acciones_juego
			if tecla == K_a:
				return (1,'ax1')
			if tecla == K_s:
				return (1, 'ax2')
			if tecla == K_z:
				return (1, 'ax3')
			if tecla == K_x:
				return (1, 'ax4')
			if tecla == K_b:
				return (1, 'ax5')
			
            #Direcciones_juego
			if tecla == K_UP:
				return (1, 'arriba')
			if tecla == K_DOWN:
				return (1,'abajo')
			if tecla == K_LEFT:
				if tecla == K_UP:
					return (1, 'arizq')
				elif tecla == K_DOWN:
					return (1, 'abizq')
				else:
					return (1, 'izquierda')
			if tecla == K_RIGHT:
				if tecla == K_UP:
					return (1, 'ardrc')
				elif tecla == K_DOWN:
					return (1, 'abdrc')
				else:
					return (1, 'derecha')
            #	else:
            #	return (0,'')
                    
		#Control_teclado_teclas_liberadas
		if event.type == KEYUP:
            if tecla == K_a:
                return (0,'ax1')
            elif tecla == K_s:
                return (0,'ax2')
            elif tecla == K_z:
                return (0,'ax3')
            elif tecla == K_x:
                return (0,'ax4')
            elif tecla == K_b:
                return (0,'ax5')
            elif tecla == K_UP:     #Direccion
				return (0, 'arriba')
			elif tecla == K_DOWN:
				return (0,'abajo')
			elif tecla == K_LEFT:
				return (0, 'izquierda')
			elif tecla == K_RIGHT:
				return (0, 'derecha')
			else:
				return (0,'')
                    
	#Control_Mouse
	def raton(self,event,mboton):
		#obtener_posicion_avanzar_click_izq
		if event.type == MOUSEBUTTONDOWN and mboton == LEFT:
			x2,y2 = event.pos
			return (x2,y2)
		#Abierto_a_una_segunda_accion
	

	#Control_USB_
	def  controler_pad(self,control):
		#Configuracion_control_=_teclado
		if control == 1:
			mando = pygame.joystick.Joystick(0)
			mando.init()
			palancas = mando.get_numballs()
			ejes = mando.get_numaxes()
			dx,dy=0,0
			botones = [mando.get_buttons]
			if palancas > 0:
				dx,dy= mando.get_ball(0)
			else:
				if ejes < 2:
				dx = dx+int(mando.get_axis(0)*10)
				dy = dy+int(mando.get_axis(1)*10)
			return (dx,dy)
			if botones > 3:
				btna = mando.get_button(botones[0])#axt1
				btnb = mando.get_button(botones[1])#axt2
				btnc = mando.get_button(botones[2])#axt3
				btnd = mando.get_button(botones[3])#axt4
#               btnstart= mando.get_button(botones[?])
        
#   if event.JOYBUTTONDOWN:

			


















	
		
		
			
