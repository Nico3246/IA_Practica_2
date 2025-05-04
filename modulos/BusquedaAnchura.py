
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
        cola.put((E[0],E[1],0))
        self.visitados[self.fila_e][self.columna_e] = True

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha
        contE = 1
        MaxCnt = contE
        maxProf=0
        encontrado=False

        while not cola.empty():
            xo,yo,prof=cola.get()

            if contE > MaxCnt:
                MaxCnt=contE

            contE -=1

            if prof>maxProf:
                maxProf = prof




            if (xo,yo) == (S[0],S[1]):
                print("Solucion encontrada usando el algoritmo Busqueda en anchura")
                encontrado=True

            else:
                x,y=xo,yo
                for i,j in movimientos:
                    fila_sig = x + i
                    columna_sig = y + j
                    if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                        if not self.visitados[fila_sig][columna_sig]:
                            self.visitados[fila_sig][columna_sig] = True
                            cola.put((fila_sig, columna_sig,prof+1))
                            contE += 1
                            self.padre[fila_sig][columna_sig] = x,y

        if encontrado:
            self.pintar_camino()
            self.caminoRecorrido()
            print("Nodos expandidos: " + self.nodosExpandidos())
            print("Numeros maximos en estructura de datos COLA: " + str(MaxCnt))
            print("Profundidad maxima alcanzada: " + str(maxProf))

        else:
            print("No se ha encontrado la salida")

    def pintar_camino(self):
        camino = []
        actual = (self.fila_s, self.columna_s)
        while actual != (self.fila_e, self.columna_e):
            camino.append(actual)
            actual = self.padre[actual[0]][actual[1]]
            if actual is None:
                break
        camino.append((self.fila_e, self.columna_e))

        for (i, j) in camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"


    def caminoRecorrido(self):
        print("Camino Recorrido (x,y): ")
        for i in range(len(self.padre)):
            for j in range(len(self.padre[0])):
                if self.padre[i][j] is not None:
                    print("[",i,",",j,"],",end=" ")
        print()


    def nodosExpandidos(self):
        nodos = 0
        for i in range(len(self.visitados)):
            for j in range(len(self.visitados[0])):
                if self.visitados[i][j]:
                    nodos += 1
        return str(nodos)


















