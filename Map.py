import sys
import pygame

pygame.init()

TAMANO_CELDA = 40


COLOR_PISO = (34, 139, 34)  
COLOR_MURO = (70, 70, 70)  
COLOR_ESTRUCTURA = (180, 180, 180)  
COLOR_ENTRADA = (34, 139, 34)  
COLOR_SALIDA = (34, 139, 34)  
COLOR_GRID = (30, 120, 30)

# ---------------------------------------------------------------------
# LEYENDA:
# 1 = Muro exterior (Gris)
# 0 = Piso libre (Verde)
# 2 = Estructura interna (Bloque gris claro)
# 8 = Entrada en el muro izquierdo (Abertura verde)
# 9 = Salida en el muro derecho (Abertura roja)
# ---------------------------------------------------------------------


mapa1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],  
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


mapa2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],  
    [1, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1],
    [1, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


mapa3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],  
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

mapas = [mapa1, mapa2, mapa3]
indice_mapa_actual = 0

FILAS = len(mapa1)
COLUMNAS = len(mapa1[0])
ANCHO_PANTALLA = COLUMNAS * TAMANO_CELDA
ALTO_PANTALLA = FILAS * TAMANO_CELDA + 50

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Mapa Bomberman - Entrada y Salida en Paredes")
fuente = pygame.font.SysFont("Consolas", 15, bold=True)


def dibujar(matriz):
    pantalla.fill(COLOR_PISO)

    # Rejilla del piso
    for x in range(0, ANCHO_PANTALLA, TAMANO_CELDA):
        pygame.draw.line(
            pantalla, COLOR_GRID, (x, 0), (x, FILAS * TAMANO_CELDA)
        )
    for y in range(0, FILAS * TAMANO_CELDA, TAMANO_CELDA):
        pygame.draw.line(
            pantalla, COLOR_GRID, (0, y), (ANCHO_PANTALLA, y)
        )

    for fila in range(FILAS):
        for col in range(COLUMNAS):
            valor = matriz[fila][col]
            x = col * TAMANO_CELDA
            y = fila * TAMANO_CELDA
            rect = pygame.Rect(x, y, TAMANO_CELDA, TAMANO_CELDA)

            # 1. Pared Externa
            if valor == 1:
                pygame.draw.rect(pantalla, COLOR_MURO, rect)
                pygame.draw.rect(
                    pantalla, (40, 40, 40), rect, width=2
                )  

            # 2. Bloques internos
            elif valor == 2:
                pygame.draw.rect(
                    pantalla, COLOR_ESTRUCTURA, rect, border_radius=4
                )
                pygame.draw.rect(
                    pantalla, (230, 230, 230), rect, width=2, border_radius=4
                )

            # 8. ENTRADA
            elif valor == 8:
                pygame.draw.rect(pantalla, COLOR_ENTRADA, rect)
                # Flecha indicando entrada ->
                pygame.draw.polygon(
                    pantalla,
                    (255, 255, 255),
                    [(x + 10, y + 10), (x + 30, y + 20), (x + 10, y + 30)],
                )

            # 9. SALIDA
            elif valor == 9:
                pygame.draw.rect(pantalla, COLOR_SALIDA, rect)
                # Flecha indicando salida ->
                pygame.draw.polygon(
                    pantalla,
                    (255, 255, 255),
                    [(x + 10, y + 10), (x + 30, y + 20), (x + 10, y + 30)],
                )

    # Texto inferior
    texto = fuente.render(
        f"MAPA: {indice_mapa_actual + 1}/3 | Presiona 1, 2 o 3 para cambiar",
        True,
        (255, 255, 255),
    )
    pantalla.blit(texto, (10, ALTO_PANTALLA - 35))


ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                indice_mapa_actual = 0
            elif evento.key == pygame.K_2:
                indice_mapa_actual = 1
            elif evento.key == pygame.K_3:
                indice_mapa_actual = 2

    dibujar(mapas[indice_mapa_actual])
    pygame.display.flip()

pygame.quit()
sys.exit()
