
import random


class BusquedaProfundidad:
    def __init__(self, lab):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada() #guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida() #guarda las coordenadas de la salida
        self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.camino = []

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
        E = self.buscar_entrada()
        S = self.buscar_salida()

        pila = [((self.fila_e, self.columna_e),0)]
        self.visitados[self.fila_e][self.columna_e] = True
        self.camino.append((self.fila_e, self.columna_e))

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha
        encontrado = False
        contE = 1
        MaxCnt = contE
        maxProf = 0

        while pila:
            (x,y),prof = pila[-1] #miro el ultimo elemento de la pila

            if len(pila) > MaxCnt:
                MaxCnt = len(pila)

            contE -= 1

            if prof > maxProf:
                maxProf = prof

            if (x, y) == (S[0], S[1]):
                print("Solucion encontrada usando el algoritmo Busqueda en profundidad")
                self.pintar_camino()
                encontrado = True
                break

            opc = []
            for i,j in movimientos:
                fila_sig = x + i
                columna_sig = y + j

                if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                    opc.append((fila_sig, columna_sig))

            if not opc:
                print("No hay solucion")
                return

            noVisitados = []
            for i in opc:
                if not self.visitados[i[0]][i[1]]:
                    noVisitados.append(i)

            if noVisitados:
                alea = random.randint(0,len(noVisitados)-1)
                seleccion = noVisitados[alea]
                self.visitados[seleccion[0]][seleccion[1]] = True
                pila.append((seleccion,prof+1))
                self.camino.append(seleccion)
            else: #si no hay casilla no visitadas retocede
               pila.pop()
               self.camino.pop()


        if encontrado:
            self.pintar_camino()
            self.caminoRecorrido()
            print("Nodos expandidos: " + self.nodosExpandidos())
            print("Numeros maximos en estructura de datos PILA: " + str(MaxCnt))
            print("Profundidad maxima alcanzada: " + str(maxProf))
        else:
            print("No se ha encontrado la salida")



    def pintar_camino(self):
        for (i, j) in self.camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "."


    def caminoRecorrido(self):
        print("Camino Recorrido (x,y): ")
        for i, j in self.camino:
            print("[", i, ",", j, "],", end=" ")
        print()


    def nodosExpandidos(self):
        nodos = 0
        for i in range(len(self.visitados)):
            for j in range(len(self.visitados[0])):
                if self.visitados[i][j]:
                    nodos += 1
        return str(nodos)
















