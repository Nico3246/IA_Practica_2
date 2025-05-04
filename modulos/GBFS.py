
from queue import PriorityQueue
from Heuristicas import Heuristica


class GBFS:
    def __init__(self, lab, nombre):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada()  # guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida()  # guarda las coordenadas de la salida
        self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla corresponde a una del laberinto y va guardando las veces que se visita
        self.camino = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]
        self.visitados[self.fila_e][self.columna_e] = True
        self.heuris = Heuristica(nombre)


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


    def heuristica(self, fila_actual, columna_actual , fila_s, columna_s):
        return self.heuris.devolverHeuristica(fila_actual, columna_actual, fila_s, columna_s)

    def moverse(self): #algoritmo A*
        E = self.buscar_entrada()
        S = self.buscar_salida()
        fila_s , columna_s = S
        h = self.heuristica(E[0], E[1],fila_s,columna_s ) #heuristica
        abierta = PriorityQueue()
        abierta.put((h, E[0], E[1]))
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha
        encontrado = False
        contE = 1
        MaxCnt = contE

        while not abierta.empty():
            h,x,y= abierta.get()

            self.visitados[x][y] = True

            if contE > MaxCnt:
                MaxCnt=contE

            contE -= 1

            if (x, y) == (S[0], S[1]):
                print("Solucion encontrada usando el algoritmo GBFS")
                encontrado = True
                break


            for i,j in movimientos:
                fila_sig = x + i
                columna_sig = y + j

                if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                    h_nuevo = self.heuristica(fila_sig, columna_sig,columna_s,fila_s )

                    if self.visitados[fila_sig][columna_sig] == False:
                        self.camino[fila_sig][columna_sig] = (x, y) #almacena el camino
                        abierta.put((h_nuevo, fila_sig, columna_sig)) #agrega la posible posicion a la cola
                        contE += 1


        if encontrado:
            self.pintar_camino()
            self.caminoRecorrido()
            print("Nodos expandidos: " + self.nodosExpandidos())
            print("Numeros maximos en estructura de datos COLA: " + str(MaxCnt))
        else:
            print("No se ha encontrado la salida")



    def pintar_camino(self):
        x , y = self.buscar_salida()
        while self.camino[x][y] is not None:
            x, y = self.camino[x][y]
            if self.lab.tabla[x][y] != "S" and self.lab.tabla[x][y] != "E":
                self.lab.tabla[x][y] = "+"


    def caminoRecorrido(self):
        print("Camino Recorrido (x,y): ")
        for i in range(len(self.camino)):
            for j in range(len(self.camino[0])):
                if self.camino[i][j] is not None:
                    print("[",i,",",j,"],",end=" ")
        print()


    def nodosExpandidos(self):
        nodos = 0
        for i in range(len(self.visitados)):
            for j in range(len(self.visitados[0])):
                if self.visitados[i][j]:
                    nodos += 1
        return str(nodos)



















