
class ProfIterativa:
    def __init__(self,lab):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada()  # guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida()  # guarda las coordenadas de la salida
        self.camino=[]

    def buscar_entrada(self):
        for i in range(len(self.lab.tabla)):
            for j in range(len(self.lab.tabla[i])):
                if self.lab.tabla[i][j] == "E":
                    return i, j
        return None, None

    def buscar_salida(self):
        for i in range(len(self.lab.tabla)):
            for j in range(len(self.lab.tabla[i])):
                if self.lab.tabla[i][j] == "S":
                    return i, j
        return None, None

    def moverse(self):
        limite=1
        cnt=0

        while True:
            self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
            self.camino = []
            resultado=self.limite(self.fila_e, self.columna_e,limite)
            if resultado:
                print("Solucion encontrada usando el algoritmo Busqueda en profundiad iterativa" )
                self.pintar_camino()
                self.caminoRecorrido()
                print("Nodos expandidos: " + self.nodosExpandidos())
                print("Profundidad maxima alcanzada: " + str(limite))
                return

            limite+=1
            cnt+=1


    def limite(self, x, y, limite):
        if (x,y) == (self.fila_s, self.columna_s):
            self.camino.append((x,y))
            return True

        if limite == 0:
            return False

        self.visitados[x][y]=True
        self.camino.append((x,y))

        movimientos=[(-1,0), (1,0), (0,-1), (0,1)]

        for i,j in movimientos:
            f=x+i
            c=y+j

            if 0 <= f < len(self.lab.tabla) and 0 <= c < len(self.lab.tabla[0]):
                if (self.lab.tabla[f][c] == " " or self.lab.tabla[f][c] == "." or self.lab.tabla[f][c] == "S") and not self.visitados[f][c]:
                    if self.limite(f,c,limite - 1):
                        return True

        self.camino.pop()
        return False

    def pintar_camino(self):
        for (i, j) in self.camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"

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

