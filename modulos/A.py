
from queue import PriorityQueue
from Heuristicas import Heuristica

class A:
    def __init__(self, lab, nombre):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada()  # guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida()  # guarda las coordenadas de la salida
        self.visitados = [[100 for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla corresponde a una del laberinto y va guardando las veces que se visita
        self.camino = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]
        self.visitados[self.fila_e][self.columna_e] = 0
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
        g = 0 #costo actual
        f = g + h #costo total estimado
        abierta = PriorityQueue()
        abierta.put((f, g, h, E[0], E[1]))
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha
        cnt = 0
        encontrado = False

        while not abierta.empty():
            f,g,h,x,y= abierta.get()
            if (x, y) == (S[0], S[1]):
                print("El agente deliberativo ha encontrado la salida en la posicion: " + str(x) + " , " + str(y) + " en " + str(cnt) + " iteraciones")
                self.pintar_camino(S)
                encontrado = True
                return

            for i,j in movimientos:
                fila_sig = x + i
                columna_sig = y + j

                if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                    g_nuevo = g+1
                    h_nuevo = self.heuristica(fila_sig, columna_sig,columna_s,fila_s )
                    f_nuevo = g_nuevo + h_nuevo

                    if self.visitados[fila_sig][columna_sig] == 0 or g_nuevo < self.visitados[fila_sig][columna_sig]: #Si g_nuevo es menor que el costo que habia en esa casilla
                        self.visitados[fila_sig][columna_sig] = g_nuevo
                        self.camino[fila_sig][columna_sig] = (x, y) #almacena el camino
                        abierta.put((f_nuevo, g_nuevo, h_nuevo, fila_sig, columna_sig)) #agrega la posible posicion a la cola
            cnt+=1
        if encontrado == False:
            print("No se ha encontrado la salida")



    def pintar_camino(self,S):
        x , y = S
        while self.camino[x][y] is not None:
            x, y = self.camino[x][y]
            if self.lab.tabla[x][y] != "S" and self.lab.tabla[x][y] != "E":
                self.lab.tabla[x][y] = "+"


















