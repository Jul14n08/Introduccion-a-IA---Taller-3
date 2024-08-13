import pygame
import sys

x_color = (255, 0, 0)
o_color = (0, 0, 255)

def dibujar_tablero(screen):
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (x * 100, 0), (x * 100, 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, x * 100), (300, x * 100), 5)

def pintar_casilla(screen, tablero, font):
    for fila in range(3):
        for columna in range(3):
            mark = tablero[fila][columna]
            if mark:
                x = columna * 100 + 100 // 2
                y = fila * 100 + 100 // 2
                text_surface = font.render(mark, True, x_color if mark == 'X' else o_color)
                text_rect = text_surface.get_rect(center=(x, y))
                screen.blit(text_surface, text_rect)

def check_ganador(tablero, mark):
    # Verificar filas y columnaumnas
    for i in range(3):
        if (all(tablero[i][j] == mark for j in range(3)) or all(tablero[j][i] == mark for j in range(3))):
            return True
        
    # Verificar diagonales
    if (all(tablero[i][i] == mark for i in range(3)) or
            all(tablero[i][2-i] == mark for i in range(3))):
        return True

    return False

def min_max(tablero):
    # TODO: Aqui debe estar la lógica de la máquina para jugar con min-max
    
    
    # Codigo de prueba para mirar que ponga la casilla la maquina
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == '':
                tablero[fila][columna] = 'O'
                return
    

def main():
    
    while True:
        response = input("¿Quién comienza? Jugador (X) o maquina (O): ")
        if response == 'X' or response == 'O':
            jugador_actual = response
            break
        else:
            print("Por favor, introduce 'X' o 'O'.")
    
    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Taller 3 - Triqui")
    font = pygame.font.Font(None, 90)
    tablero = [['' for _ in range(3)] for _ in range(3)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                columna = x // 100
                fila = y // 100
                
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = jugador_actual
                    
                    # Verifica que haya ganador
                    if check_ganador(tablero, jugador_actual):
                        print(f"{jugador_actual} gana")
                        running = False
                    else:
                        # Verifica si esta lleno el tablero y no hay ganador
                        if all(all(fila) for fila in tablero):
                            print("Empate")
                            running = False
                            
                    #Cambio de jugador
                    if jugador_actual == 'X': 
                        jugador_actual = 'O'
                    else:
                        jugador_actual = 'X'
                        
        if jugador_actual == 'O' and running:
            min_max(tablero)
            if check_ganador(tablero, 'O'):
                print("O gana")
                running = False
            jugador_actual = 'X'

        screen.fill((255, 255, 255))
        dibujar_tablero(screen)
        pintar_casilla(screen, tablero, font)
        pygame.display.flip()

if __name__ == "__main__":
    main()
