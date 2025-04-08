import random

class laberinto:

    def __init__(self):
        self.x = random.randint(10,20)
        self.y = random.randint(15,20)
        #Crear la tabla en el que estara el laberinto con un tamañano aleatorio
        self.tabla=[[" " for _ in range(self.y)] for _ in range(self.x)]

    def crearlaberinto(self):
        #selecciona dos filas aleatorias para E y S. Para evitar que se cree en las esquinas el rango es 1 y self.x -2
        fila_e=random.randint(1,self.x-2)
        fila_s=random.randint(1,self.x-2)

        #Creamos los bordes
        for i in range(self.x):
            for j in range(self.y):
                self.tabla[i][0]="#"
                self.tabla[i][self.y-1]="#"
                self.tabla[0][j]="#"
                self.tabla[self.x-1][j]="#"

        #Creamos las posiciones de entraday salida del laberinto
        self.tabla[fila_e][0] = "E"
        self.tabla[fila_s][self.y - 1] = "S"


        #Crear camino
        pos1 = fila_e
        pos2 = 0
        opciones1 = []
        opciones2 = []

        while pos1 != fila_s or pos2 != self.y-1:


            if self.tabla[pos1-1][pos2]==" ":  #arriba
                opciones1.append(pos1-1)
                opciones2.append(pos2)

            if self.tabla[pos1+1][pos2]==" ":#abajo
                opciones1.append(pos1+1)
                opciones2.append(pos2)

            if self.tabla[pos1][pos2+1]==" ":#derecha
                opciones1.append(pos1)
                opciones2.append(pos2+1)
            elif self.tabla[pos1][pos2+1]=="S":
                break

            if self.tabla[pos1][pos2 + 1] == "#":
                if pos1 < fila_s:  #si la salida está más abajo nos movemos hacia abajo
                    while pos1 != fila_s and self.tabla[pos1 + 1][pos2] != "#":
                        opciones1.append(pos1 + 1)
                        opciones2.append(pos2)
                        self.tabla[pos1][pos2] = "o"
                        pos1 += 1
                elif pos1 > fila_s:  #si la salida está más arriba nos movemos hacia arriba
                    while pos1 != fila_s and self.tabla[pos1 - 1][pos2] != "#":
                        opciones1.append(pos1 - 1)
                        opciones2.append(pos2)
                        self.tabla[pos1][pos2] = "o"
                        pos1 -= 1

            if opciones1:  # si la tabla esta llena
                opc = random.randint(0, len(opciones1) - 1)
                pos1 = opciones1[opc]
                pos2 = opciones2[opc]
            else:
                break


            self.tabla[pos1][pos2] = "o"

            opciones1.clear()
            opciones2.clear()


        #colocar obstaculos
        for i in range(self.x-1):
            for j in range(self.y-1):
                if self.tabla[i][j]!="o" and self.tabla[i][j]!="E" and self.tabla[i][j]!="S" :
                    alea = random.randint(0, 1)
                    if alea == 1:
                        self.tabla[i][j] = "#"

        #quitar o
        for i in range(self.x):
            for j in range(self.y):
                if self.tabla[i][j]=="o":
                    self.tabla[i][j] = " "

    def guardarLaberinto(self):

        f = open("Laberinto.txt", "w")
        for i in range(self.x):
            for j in range(self.y):
                f.write(self.tabla[i][j])
            f.write("\n")
        f.close()

    def cargarLaberinto(self,archivo):
        f = open(archivo, "r")
        lineas = f.readlines()
        f.close()

        self.x = len(lineas)#cantidad de columnas
        self.y = len(lineas[0].strip())#cantidad de filas

        # Crear tabla con el tamaño del fihero
        self.tabla = [[" " for _ in range(self.y)] for _ in range(self.x)]

        for i in range(len(lineas)):
            linea_actual = lineas[i].strip()
            for j in range(len(linea_actual)):
                self.tabla[i][j] = linea_actual[j]


    def posicionE(self):
        fila_e = 0
        columna_e = 0
        es1 = False
        for i in range(self.x):
            if self.tabla[i][0]=="E":
                fila_e=i
            elif self.tabla[i][1]=="E":
                es1 = True
                fila_e=i
        if es1:
            print("Posicion de entrada: " + str(fila_e) + " , 1")
        else:
            print("Posicion de entrada: " + str(fila_e) + " , 0")
        return fila_e

    def posicionS(self):
        fila_s = 0
        es1 = False
        for i in range(self.x):
            if self.tabla[i][self.y - 1] == "S":
                fila_s = i
            elif self.tabla[i][self.y - 2] == "S":
                es1 = True
                fila_s = i

        if es1:
            print("Posicion de salida: " + str(fila_s) + " , " + str(self.y - 2))
        else:
            print("Posicion de salida: " + str(fila_s) + " , " + str(self.y - 1))

    def mostrarLaberinto(self):

        for i in range(self.x):
            for j in range(self.y):
                print(self.tabla[i][j], end=" ")
            print()

        self.posicionE()
        self.posicionS()

