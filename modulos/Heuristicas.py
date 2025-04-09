import math

class Heuristica:
    def __init__(self,nombre):
         self.nombre = nombre

    def Manhattan(self,pos1,pos2,columna_s,fila_s):
        return abs(pos1 - fila_s) + abs(pos2 - columna_s)

    def Euclidia(self,pos1,pos2,columna_s,fila_s):
        return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2)

    def personal(self,pos1,pos2,columna_s,fila_s):
        #return abs(fila_s - pos1) + abs(columna_s - pos2) + 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))  #manhattan pero penalizq alejarse o desviarse de la meta premia ir en linea recta
        #return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2) * 1.5
        #return 1.5 * (abs(fila_s - pos1) + abs(columna_s - pos2)) + 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))
        #return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2) * 1.5 + 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))



    def devolverHeuristica(self,pos1,pos2,columna_s,fila_s):
        if self.nombre == "Manhattan":
            return self.Manhattan(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Euclidia":
            return self.Euclidia(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal":
            return self.personal(pos1,pos2,columna_s,fila_s)