import math

class Heuristica:
    def __init__(self,nombre):
         self.nombre = nombre

    def Manhattan(self, fila_actual, columna_actual, fila_s, columna_s):
        return abs(fila_actual - fila_s) + abs(columna_actual - columna_s)

    def Euclidia(self, fila_actual, columna_actual, fila_s, columna_s):
        return math.sqrt((fila_actual - fila_s) ** 2 + (columna_actual - columna_s) ** 2)

    def personal(self, fila_actual, columna_actual, fila_s, columna_s):
        return abs(columna_s - fila_actual) + abs(fila_s - columna_actual) + 0.1 * max(abs(columna_s - fila_actual), abs(fila_s - columna_actual))  #manhattan pero penalizq alejarse o desviarse de la meta premia ir en linea recta
        #esta es la mas eficiente en la amyoria de casos


     #pueden tener problemas de admisibilidad, arregladas podrian ser:


    """def personal2(self, fila_actual, columna_actual, columna_s, fila_s):
        return math.sqrt((fila_actual - fila_s)**2 + (columna_actual - columna_s)**2) * 1.5

    def personal3(self, fila_actual, columna_actual, columna_s, fila_s):
        return 1.5 * (abs(fila_s - fila_actual) + abs(columna_s - columna_actual)) + 0.1 * max(abs(fila_s - fila_actual), abs(columna_s - columna_actual))

    def personal4(self, fila_actual, columna_actual, columna_s, fila_s):
        return math.sqrt((fila_actual - fila_s) ** 2 + (columna_actual - columna_s) ** 2) * 1.5 + 0.1 * max(abs(fila_s - fila_actual))

    #arregladas supuestamente                                                                  abs(columna_s - columna_actual))
    def personal5(self, fila_actual, columna_actual, columna_s, fila_s):
        return abs(fila_s - fila_actual) + abs(columna_s - columna_actual) - 0.1 * max(abs(fila_s - fila_actual), abs(columna_s - columna_actual))

    def personal6(self, fila_actual, columna_actual, columna_s, fila_s):
        return math.sqrt((fila_actual - fila_s)**2 + (columna_actual - columna_s)**2)

    def personal7(self, fila_actual, columna_actual, columna_s, fila_s):
        return abs(fila_s - fila_actual) + abs(columna_s - columna_actual) - 0.1 * max(abs(fila_s - fila_actual), abs(columna_s - columna_actual))

    def personal8(self, fila_actual, columna_actual, columna_s, fila_s):
        return math.sqrt((fila_s - fila_actual)**2 + (columna_s - columna_actual)**2) - 0.1 * max(abs(fila_s - fila_actual), abs(columna_s - columna_actual))



"""



    def devolverHeuristica(self,fila_actual,columna_actual,columna_s,fila_s):
        if self.nombre == "Manhattan":
            return self.Manhattan(fila_actual,columna_actual,columna_s,fila_s)
        elif self.nombre == "Euclidia":
            return self.Euclidia(fila_actual,columna_actual,columna_s,fila_s)
        elif self.nombre == "Personal":
            return self.personal(fila_actual, columna_actual, columna_s, fila_s)
