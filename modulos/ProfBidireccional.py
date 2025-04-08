import queue


class ProfBidireccional:
    def __init__(self, lab):
        self.lab = lab
        self.Entrada = self.buscar_entrada()  # guarda las coordenadas de la entrada
        self.Salida = self.buscar_salida()  # guarda las coordenadas de la salida
        self.visitadosInicio = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(
            len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.visitadosMeta = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(
            len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.padreInicio = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(
            len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.padreMeta = [[None for _ in range(len(self.lab.tabla[0]))] for _ in range(
            len(self.lab.tabla))]  # crea una tabla del tamaño del laberinto en la que cada casilla cor
        self.colaInicio = queue.Queue()
        self.colaMeta = queue.Queue()

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
        self.colaInicio.put(self.Entrada)
        self.colaMeta.put(self.Salida)

        self.visitadosInicio[self.Entrada[0]][self.Entrada[1]] = True
        self.visitadosMeta[self.Salida[0]][self.Salida[1]] = True

        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba,abajo,izquierda,derecha

        while not self.colaInicio.empty() and not self.colaMeta.empty():
            actualInicio = self.colaInicio.get()
            actualMeta = self.colaMeta.get()

            # Expansion desde la entrada
            for i, j in movimientos:
                x = actualInicio[0] + i
                y = actualInicio[1] + j

                if self.lab.tabla[x][y] == " " or self.lab.tabla[x][y] == "." or self.lab.tabla[x][y] == "S":
                    if not self.visitadosInicio[x][y]:
                        self.visitadosInicio[x][y] = True
                        self.padreInicio[x][y] = actualInicio
                        self.colaInicio.put((x, y))

                        if self.visitadosMeta[x][y] == True:
                            interseccion = (x, y)
                            return self.pintar_camino(interseccion)

            # expansion desde la salida
            for i, j in movimientos:
                x = actualMeta[0] + i
                y = actualMeta[1] + j

                if self.lab.tabla[x][y] == " " or self.lab.tabla[x][y] == "." or self.lab.tabla[x][y] == "S":
                    if not self.visitadosMeta[x][y]:
                        self.visitadosMeta[x][y] = True
                        self.padreMeta[x][y] = actualMeta
                        self.colaMeta.put((x, y))

                        if self.visitadosInicio[x][y] == True:
                            interseccion = (x, y)
                            return self.pintar_camino(interseccion)

    def pintar_camino(self, interseccion):
        caminoTotal = []
        nodo = interseccion
        while nodo:
            caminoTotal.append(nodo)
            nodo = self.padreInicio[nodo[0]][nodo[1]]

        nodo = self.padreMeta[interseccion[0]][interseccion[1]]
        while nodo:
            caminoTotal.append(nodo)
            nodo = self.padreMeta[nodo[0]][nodo[1]]

        for (i, j) in caminoTotal:
            if self.lab.tabla[i][j] != "S" and self.lab.tabla[i][j] != "E":
                self.lab.tabla[i][j] = "-"


