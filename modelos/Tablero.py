from random import randint as numeroAleatorio


class Tablero:
    filas = 0
    columnas = 0
    tablero = [[0] * columnas] * filas
    NUMEROMINAS = 36

    def __init__(self,f,c):
        self.filas = f
        self.columnas = c
        self.tablero = [[0] * self.columnas] * self.filas

    def crearTablero(self):
        numeroMinasInsertadas = 0
        i = 0
        j = 0
        while(self.NUMEROMINAS > numeroMinasInsertadas):
            gen = numeroAleatorio(0,self.filas*self.columnas) % 2
            if(gen == 1):
                self.tablero[i%self.filas][j%self.columnas] = gen
                numeroMinasInsertadas += 1
            else:
                self.tablero[i%self.filas][j%self.columnas] = gen
            i += 1 
            j += 1

    def mostrarTablero(self):
        for i in range(0,self.filas):
            print("")
            for j in range(0,self.columnas):
                print(self.tablero[i][j], end =" ")

    def mirarAlrededor(self,f,c):
        minasAlrededor = 0
        f = f-1
        f = c-1
        
        if(self.tablero[f][c+1] == 1):
            minasAlrededor += 1
        
        if(self.tablero[f][c-1] == 1):
            minasAlrededor += 1

        if(self.tablero[f+1][c] == 1):
            minasAlrededor += 1
        
        if(self.tablero[f-1][c] == 1):
            minasAlrededor += 1
        
        """diagonales"""
        if(self.tablero[f+1][c+1] == 1):
            minasAlrededor += 1
        
        if(self.tablero[f+1][c-1] == 1):
            minasAlrededor += 1

        if(self.tablero[f-1][c+1] == 1):
            minasAlrededor += 1

        if(self.tablero[f-1][c-1] == 1):
            minasAlrededor += 1

        return minasAlrededor
       

    