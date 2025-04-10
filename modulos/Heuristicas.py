import math

class Heuristica:
    def __init__(self,nombre):
         self.nombre = nombre

    def Manhattan(self,pos1,pos2,columna_s,fila_s):
        return abs(pos1 - fila_s) + abs(pos2 - columna_s)

    def Euclidia(self,pos1,pos2,columna_s,fila_s):
        return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2)

    def personal(self,pos1,pos2,columna_s,fila_s):
        return abs(fila_s - pos1) + abs(columna_s - pos2) + 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))  #manhattan pero penalizq alejarse o desviarse de la meta premia ir en linea recta
        #esta es la mas eficiente en la amyoria de casos

     #pueden tener problemas de admisibilidad, arregladas podrian ser:


    """def personal2(self, pos1, pos2, columna_s, fila_s):
        return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2) * 1.5

    def personal3(self, pos1, pos2, columna_s, fila_s):
        return 1.5 * (abs(fila_s - pos1) + abs(columna_s - pos2)) + 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))

    def personal4(self, pos1, pos2, columna_s, fila_s):
        return math.sqrt((pos1 - fila_s) ** 2 + (pos2 - columna_s) ** 2) * 1.5 + 0.1 * max(abs(fila_s - pos1))

    #arregladas supuestamente                                                                  abs(columna_s - pos2))
    def personal5(self, pos1, pos2, columna_s, fila_s):
        return abs(fila_s - pos1) + abs(columna_s - pos2) - 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))

    def personal6(self, pos1, pos2, columna_s, fila_s):
        return math.sqrt((pos1 - fila_s)**2 + (pos2 - columna_s)**2)

    def personal7(self, pos1, pos2, columna_s, fila_s):
        return abs(fila_s - pos1) + abs(columna_s - pos2) - 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))

    def personal8(self, pos1, pos2, columna_s, fila_s):
        return math.sqrt((fila_s - pos1)**2 + (columna_s - pos2)**2) - 0.1 * max(abs(fila_s - pos1), abs(columna_s - pos2))



"""



    def devolverHeuristica(self,pos1,pos2,columna_s,fila_s):
        if self.nombre == "Manhattan":
            return self.Manhattan(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Euclidia":
            return self.Euclidia(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal":
            return self.personal(pos1,pos2,columna_s,fila_s)
        #de aqui a abajo borrar
        elif self.nombre == "Personal2":
            return self.personal2(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal3":
            return self.personal3(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal4":
            return self.personal4(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal5":
            return self.personal5(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal6":
            return self.personal6(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal7":
            return self.personal7(pos1,pos2,columna_s,fila_s)
        elif self.nombre == "Personal8":
            return self.personal8(pos1,pos2,columna_s,fila_s)
