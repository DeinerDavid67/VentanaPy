import pygame
import sys


pygame.init()


ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ventana Pygame - VENTANA CLASE")


NEGRO = (18, 18, 18)
ROJO = (255, 0, 0)



fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
fuente_subtitulo = pygame.font.SysFont("arial", 22)


texto_nombre = fuente_titulo.render("¡Deiner Cuitiva!", True, ROJO)
rect_nombre = texto_nombre.get_rect(center=(ANCHO // 2, ALTO // 2 - 20))



ejecutando = True
while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

   
    ventana.fill(NEGRO)
    ventana.blit(texto_nombre, rect_nombre)
    

  
    pygame.display.flip()


pygame.quit()
sys.exit()