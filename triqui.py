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
    # Verificar filas y columnas
    for i in range(3):
        if (all(tablero[i][j] == mark for j in range(3)) or all(tablero[j][i] == mark for j in range(3))):
            return True
        
    # Verificar diagonales
    if (all(tablero[i][i] == mark for i in range(3)) or
            all(tablero[i][2-i] == mark for i in range(3))):
        return True

    return False

def tablero_lleno(tablero):
    return all(all(casilla != '' for casilla in fila) for fila in tablero)

def min_max(tablero, profundidad, is_maximizing):
    # Busca primero si de las opciones que está buscando, hay un ganador o un empate (el algoritmo va a bajar en el arbol de posibilidades hasta que alguna de las tres sentencias se cumpla, y respecto a eso hace las evaluaciones de minimizar y maximizar)
    if check_ganador(tablero, 'O'):
        return 1
    elif check_ganador(tablero, 'X'):
        return -1
    elif tablero_lleno(tablero):
        return 0
    
    # Si es el posible turno de la máquina, intentará maximizar su puntuación.
    if is_maximizing:
        mejor_puntuacion = -float('inf') # Inicializa la mejor puntuación con un valor muy bajo.
        
        #Va a analizar todas las casillas vacias (en donde se puede jugar la máquina), y llama min_max
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    
                    # Pone temporalmente O en la casilla como si hubiera jugado en esa posición
                    tablero[fila][columna] = 'O'
                    
                    # Llama recursivamente pasa simular las posibilidades que tendría jugando en esa posición
                    puntuacion = min_max(tablero, profundidad + 1, False)
                    
                    # Después de evaluar el movimiento, lo deshace para volver al estado inicial
                    tablero[fila][columna] = ''
                    
                    # Si la puntuación es mejor que en otras jugadas, lo pone en mejor puntuacion
                    mejor_puntuacion = max(mejor_puntuacion, puntuacion)
        return mejor_puntuacion
    
    # Simulando si es el turno del jugador (is_maximizing es False), intentará minimizar la puntuación de la máquina (osea la peor posibilidad que tendría).
    else:        
        peor_puntuacion = float('inf') # Inicializa la peor puntuación con un valor muy alto.
        
        #Va a analizar todas las casillas vacias (en donde se puede jugar la máquina), y llama min_max
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    
                    # Pone temporalmente X en la casilla como si hubiera jugado en esa posición
                    tablero[fila][columna] = 'X'
                    
                    # Llama min_max pasa simular las posibilidades que tendría la maquina si el jugador jugara en esa posición
                    puntuacion = min_max(tablero, profundidad + 1, True)
                    
                    # Después de evaluar el movimiento, lo deshace para volver al estado inicial
                    tablero[fila][columna] = ''
                    
                    # Si la puntuación es peor para la maquina que en otras jugadas, lo pone en peor puntuacion
                    peor_puntuacion = min(peor_puntuacion, puntuacion)
        return peor_puntuacion

def mejor_movimiento(tablero):
    mejor_puntuacion = -float('inf') #Inicializa la "Mejor" puntuación en negativo infinito y va a tratar de hallar una jugada que lo haga lo más grande posible
    movimiento = None # Aqui se guarda la mejor jugada que puede hacer con minimax
    
    #Va a analizar todas las casillas vacias (en donde se puede jugar), y llama min_max (Primero tratando de minimizar las posibilidades si jugara el jugador)
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == '':
                
                # Pone temporalmente O en la casilla como si hubiera jugado en esa posición
                tablero[fila][columna] = 'O'
                
                # Llama min_max pasa simular las posibilidades que tendría jugando en esa posición
                puntuacion = min_max(tablero, 0, False)
                
                # Después de evaluar el movimiento, lo deshace para volver al estado inicial
                tablero[fila][columna] = ''
                
                # Si la puntuación de este movimiento es mejor que la puntuación máxima conocida, se actualiza tanto el valor como la casilla que jugaría en el mejor caso.
                if puntuacion > mejor_puntuacion:
                    mejor_puntuacion = puntuacion
                    movimiento = (fila, columna)
    return movimiento

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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and jugador_actual == 'X':
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
                        if tablero_lleno(tablero):
                            print("Empate")
                            running = False
                            
                    # Cambio de jugador
                    jugador_actual = 'O'
                        
        if jugador_actual == 'O' and running:
            movimiento = mejor_movimiento(tablero)
            if movimiento:
                tablero[movimiento[0]][movimiento[1]] = 'O'
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
