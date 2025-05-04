
import random
class ProfLimite:
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

    def moverse(self,limite):
        E = self.buscar_entrada()
        S = self.buscar_salida()

        pila = [(self.fila_e, self.columna_e)]
        self.visitados[self.fila_e][self.columna_e] = True
        self.camino.append((self.fila_e, self.columna_e))

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #arriba,abajo,izquierda,derecha

        contE = 1
        MaxCnt = contE
        encontrado = False

        while pila:
            pos = pila[-1] #miro el ultimo elemento de la pila
            x,y = pos
            if (x, y) == (S[0], S[1]):
                encontrado=True
                break

            if len(pila) > MaxCnt:
                MaxCnt=len(pila)


            prof=len(self.camino) - 1
            if prof >= limite:
                pila.pop()
                self.camino.pop()
                continue


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
                pila.append(seleccion)
                self.camino.append(seleccion)
            else: #si no hay casilla no visitadas retocede
               pila.pop()
               self.camino.pop()


        if encontrado:
            self.pintar_camino()
            self.caminoRecorrido()
            print("Nodos expandidos: " + self.nodosExpandidos())
            print("Numeros maximos en estructura de datos PILA: " + str(MaxCnt))
            print("Profundidad maxima alcanzada: " + str(limite))

        else:
            print("No se ha encontrado la salida")





    def pintar_camino(self):
        for (i, j) in self.camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"


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















