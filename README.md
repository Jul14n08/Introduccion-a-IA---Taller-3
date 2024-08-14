# Introduccion a IA Taller-3 GRUPO 3

El objetivo del taller consiste en jugar triqui contra la máquina, la cual toma sus desiciones de acuerdo a un algoritmo MIN-MAX.

## Requisitos

- Python3
- Pygame

### Instalar librería de Pygame
```bash
pip install pygame
```

## Cómo jugar

Al iniciar el juego, se te preguntará en consola quién debe comenzar: (Jugador o la maquina), luego se abre el tablero y seleccionas la casilla que quieres jugar.

Al final del juego, en consola se imprime quien gano el juego, o si hubo un empate.

## Estructura del código

El código se organiza en las siguientes funciones:
- `dibujar_tablero(screen)`: Dibuja las líneas del tablero.
- `pintar_casilla(screen, tablero, font)`: Pinta las casillas de los jugadores en el tablero.
- `check_ganador(tablero, mark)`: Verifica si ha ganado alguien y quien.
- `min_max(tablero)`: Lógica de juego de la máquina.

## Ejecución

```bash
python triqui.py
```


## Estados
Estado: El estado es la configuración actual del tablero, representada como una matriz de 3x3 con casillas vacías, 'X' o 'O'. En cualquier momento, el estado define cuál es la situación actual del juego.
Ejemplos de posibles estados:

Estado inicial (tablero vacío):

 ['', '', ''], 
 ['', '', ''],
 ['', '', '']
Estado después de algunos movimientos:

['X', '', 'O'], 
['O', 'X', ''], 
['', '', '']
Estado terminal (jugador X gana):


['X', '', 'O'], 
['O', 'X', ''],
['', '', 'X']


## Espacio problema
El espacio problema en el Tic-Tac-Toe es el conjunto de todos los posibles tableros (estados) que pueden formarse al colocar X y O en las casillas, mientras que los estados son las configuraciones actuales del tablero en cualquier punto del juego, que evolucionan a medida que los jugadores realizan sus movimientos.

## Minimax y la Función Heurística

Valor +1: si la IA (jugador 'O') gana.
Valor -1: si el jugador humano (jugador 'X') gana.
Valor 0: si hay empate.
