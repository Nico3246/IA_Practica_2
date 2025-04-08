
import random
import queue


class BusquedaAnchura:
    def __init__(self, lab):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada() #guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida() #guarda las coordenadas de la salida
        self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.padre = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor


    def buscar_entrada(self):
        for i in range(len(self.lab.tabla)):
            for j in range(len(self.lab.tabla[i])):
                if self.lab.tabla[i][j] == "E":
                    return i, j
        return None,None

    def buscar_salida(self):
        for i in range(len(self.lab.tabla)):
            for j in range(len(self.lab.tabla[i])):
                if self.lab.tabla[i][j] == "S":
                    return i, j
        return None,None

    def moverse(self):
        E = (self.fila_e, self.columna_e)
        S = (self.fila_s, self.columna_s)

        cola=queue.Queue()
        cola.put(E)
        self.visitados[self.fila_e][self.columna_e] = True

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha
        cnt = 0
        encontrado=False

        while not cola.empty():
            actual=cola.get()
            cnt +=1

            if actual == S:
                print("El agente deliberativo ha encontrado la salida en la posicion: " + str(actual[0]) + " , " + str(actual[1]) + " en " + cnt + " iteraciones")
                encontrado=True

            else:
                x,y=actual
                for i,j in movimientos:
                    fila_sig = x + i
                    columna_sig = y + j
                    if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                        if not self.visitados[fila_sig][columna_sig]:
                            self.visitados[fila_sig][columna_sig] = True
                            cola.put((fila_sig, columna_sig))
                            self.padre[fila_sig][columna_sig] = x,y
            if encontrado:
                self.pintar_camino()
            else:
                print("No se ha encontrado la salida")

    def pintar_camino(self,S):
        camino = []
        actual = S
        while actual != (self.fila_e, self.columna_e):
            camino.append(actual)
            actual = self.padre[actual[0]][actual[1]]
            if actual is None:
                break
        camino.append((self.fila_e, self.columna_e))

        for (i, j) in camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"


















