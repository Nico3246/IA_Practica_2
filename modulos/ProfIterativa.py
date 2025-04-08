
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

        while True:
            self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
            self.camino = []
            resultado=self.dfs_limitado(self.fila_e, self.columna_e,limite)
            if resultado:
                print("El agente deliberativo ha encontrado la salida a profundiad " + str(limite))
                self.pintar_camino()
                return

            limite+=1


    def dfs_limitado(self, x, y, limite):
        if (x,y) == (self.fila_s, self.columna_s):
            self.camino.append((x,y))
            return True

        if limite == 0:
            return False

        self.visitados[x][y]=True
        self.camino.append((x,y))

        movimientos=[(-1,0), (1,0), (0,-1), (0,1)]

        for i,j in movimientos:
            f= x+i
            c=y+j

            if 0 <= f < len(self.lab.tabla) and 0 <= c < len(self.lab.tabla[0]):
                if self.lab.tabla[f][c] in (" ", ".","S") and not self.visitados[f][c]:
                    if self.dfs_limitado(f,c,limite - 1):
                        return True

        self.camino.pop()
        return False

    def pintar_camino(self):
        for (i, j) in self.camino:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"


