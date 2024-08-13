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
