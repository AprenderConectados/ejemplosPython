#importamos las librerias que vamos a utilizar
import sys, pygame

#inicializamos la libreria pygame y mixer
pygame.init()

#creamos una pantalla de 800x600
size = 800,600
screen = pygame.display.set_mode(size)

ancho, largo = pygame.display.get_surface().get_size()

#ponemos un titulo a la ventana
pygame.display.set_caption("Juego Pelota") 

#cargamos un sonido de choque
choqueSonido = pygame.mixer.Sound("choque.wav")

#cargamos una imagen que debe estar en la misma ruta de nuestro archivo .py
pelota = pygame.image.load("pelota.png")
pelotaXY = pelota.get_rect()

#cargamos una imagen de una linea
linea = pygame.image.load("linea.png")
lineaXY = linea.get_rect()
lineaXY.move_ip(ancho/2,largo/2)

velocidad = [10,9]

ejecutar = True

#creamos el bucle del juego
while ejecutar:
		#recorremos todos los eventos que se producen en la ventana
		for event in pygame.event.get():
			#detectamos el evento de cerrar la ventana
			if event.type == pygame.QUIT: ejecutar = False
		
		#capturamos las teclas
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			lineaXY = lineaXY.move(0, -1)
		if keys[pygame.K_DOWN]:
			lineaXY = lineaXY.move(0, 1)
		
		#detecto cuando chocan la linea y la pelota
		if lineaXY.colliderect(pelotaXY):
			velocidad[0] = -velocidad[0]
			choqueSonido.play()
		
		pelotaXY = pelotaXY.move(velocidad)
		
		if pelotaXY.left < 0 or pelotaXY.right > ancho:
			velocidad[0] = -velocidad[0]
			
		if pelotaXY.top < 0 or pelotaXY.bottom > largo:
			velocidad[1] = -velocidad[1]
		
		screen.fill([255,255,255])
		screen.blit(pelota, pelotaXY)
		screen.blit(linea, lineaXY)
		pygame.display.flip()

pygame.quit()
