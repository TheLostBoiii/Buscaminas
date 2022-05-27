
from random import randint as r


class Tablero:
    filas = 0
    columnas = 0
    tablero = [[0] * columnas] * filas

    def __init__(self,f,c):
        self.filas = f
        self.columnas = c
        self.tablero = [[0] * self.columnas] * self.filas

    def crearTablero(self):
        for i in range(0,self.filas):
            for j in range(0,self.columnas):
                self.tablero[i][j] = 2

    def mostrarTablero(self):
        for i in range(0,self.filas):
            print("")
            for j in range(0,self.columnas):
                print(self.tablero[i][j], end =" ")

    