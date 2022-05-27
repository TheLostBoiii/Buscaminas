from modelos.Tablero import Tablero

tablero = Tablero(8,8)
tablero.crearTablero()
tablero.mostrarTablero()
print("\nMinas Alrededor de (3, 5): ", end=" ")
print(tablero.mirarAlrededor(3,5))

    