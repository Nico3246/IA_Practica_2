from Heuristicas import Heuristica

class IDA:
    def __init__(self, lab, nombre):
        self.lab = lab
        self.fila_e, self.columna_e = self.buscar_entrada()  # guarda las coordenadas de la entrada
        self.fila_s, self.columna_s = self.buscar_salida()  # guarda las coordenadas de la salida
        self.camino = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]
        self.visitados = [[False for _ in range(len(self.lab.tabla[0]))] for _ in range(len(self.lab.tabla))]
        self.visitados[self.fila_e][self.columna_e] = True
        self.heuris = Heuristica(nombre)


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

    def heuristica(self, fila_actual, columna_actual, fila_s, columna_s):
        return round(self.heuris.devolverHeuristica(fila_actual, columna_actual, fila_s, columna_s))

    def IDA(self,x,y,g,umbral,salida):
        h=self.heuristica(x,y,self.fila_s,self.columna_s)
        f=g+h

        if f > umbral:
            return f
        if (x,y) == salida:
            return "encontrado"

        min_val = float("inf") #min_val empieza siendo inf para q el primero siempre sea menor
        movimientos=[(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i,j in movimientos:
            fila_sig = x + i
            columna_sig = y + j

            if self.lab.tabla[fila_sig][columna_sig] == " " or self.lab.tabla[fila_sig][columna_sig] == "." or self.lab.tabla[fila_sig][columna_sig] == "S":
                self.camino[fila_sig][columna_sig] = (x,y)
                self.visitados[fila_sig][columna_sig] = True
                res=self.IDA(fila_sig, columna_sig, g+1, umbral, salida)
                if res == "encontrado":
                    self.camino[fila_sig][columna_sig] = (x, y)
                    return "encontrado"
                elif res < min_val:
                    min_val = res

        return min_val


    def moverse(self):
        E = self.buscar_entrada()
        S = self.buscar_salida()

        umbral=self.heuristica(E[0],E[1], self.fila_s, self.columna_s)

        while True: #no me gusta el true
            salida=self.IDA(E[0],E[1],0,umbral,S)

            if salida == "encontrado":
                print("Solucion encontrada usando el algoritmo IDA*")
                self.pintar_camino(S)
                self.caminoRecorrido()
                print("Nodos expandidos: " + self.nodosExpandidos())
                return

            umbral = salida

    def pintar_camino(self, S):
        x, y = S
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
