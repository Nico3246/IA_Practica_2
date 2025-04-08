from Laberinto import laberinto
from A import A
from BusquedaProfundidad import BusquedaProfundidad
from Heuristicas import Heuristica
from ProfBidireccional import ProfBidireccional
from ProfIterativa import ProfIterativa

def menu(lab,nombreHeur):
    while True:
        print("\n")
        print("MENU")
        print("1. Iniciar el algoritmo de busqueda en profundidad")
        print("2. Iniciar el algoritmo de busqueda a*")
        print("3. Iniciar el algoritmo de busqueda en anchura")
        print("4. Iniciar el algoritmo de busqueda en profundidad bidireccional")
        print("5. Iniciar el algoritmo de busqueda en profundidad iterativa")
        print("6. Reiniciar el laberinto")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            DBF = BusquedaProfundidad(lab)
            DBF.moverse()
            print("\n")
            lab.mostrarLaberinto()

        if opcion == "2":
            a = A(lab,nombreHeur)
            a.moverse()
            print("\n")
            lab.mostrarLaberinto()

        if opcion == "3":
            Bp = BusquedaProfundidad(lab)
            Bp.moverse()
            print("\n")
            lab.mostrarLaberinto()

        if opcion == "4":
            pB = BusquedaProfundidad(lab)
            pB.moverse()
            print("\n")
            lab.mostrarLaberinto()

        if opcion == "5":
            pi = ProfIterativa(lab)
            pi.moverse()
            print("\n")
            lab.mostrarLaberinto()

        if opcion == "6":
            op = input("¿Quiere reiniciar el laberinto?S/N: ")
            if op == 'S' or op == 's':
                lab.cargarLaberinto("Laberinto.txt")
                lab.mostrarLaberinto()


        if opcion == "4":
            break

def menuH(lab):
    while True:
        print("\n")
        print("MENU")
        print("Seleccione una heuristica a utilizar: ")
        print("1. Manhattan")
        print("2. Euclidia")
        print("3. Personal")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            return "Manhattan"


        if opcion == "2":
            return "Euclidia"


        if opcion == "3":
            return "Personal"


        if opcion == "4":
            return None




def main():
    lab = laberinto()

    print("\n")
    print("MENU")
    print("1. Crear laberinto")
    print("2. Cargar maze1.txt")
    print("3. Cargar maze2.txt")
    print("4. Cargar maze3.txt")
    print("5. Cargar laberinto guardado")
    print("6. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        lab.crearlaberinto()
        print("\n")
        print("Laberinto generado:")
        lab.mostrarLaberinto()
        print("\n")

        opcion2 = input("Quiere guardar el laberinto?S/N: ")
        if opcion2 == 'S' or opcion2 == 's':
            lab.guardarLaberinto()
            print("\n")
            print("Laberinto guardado")
            print("\n")

    elif opcion == "2":
        lab.cargarLaberinto("maze1.txt")
        print("\n")
        print("Laberinto generado:")
        lab.mostrarLaberinto()
        print("\n")

    elif opcion == "3":
        lab.cargarLaberinto("maze2.txt")
        print("\n")
        print("Laberinto generado:")
        lab.mostrarLaberinto()
        print("\n")

    elif opcion == "4":
        lab.cargarLaberinto("maze3.txt")
        print("\n")
        print("Laberinto generado:")
        lab.mostrarLaberinto()
        print("\n")

    elif opcion == "5":
        lab.cargarLaberinto("Laberinto.txt")
        print("\n")
        print("Laberinto generado:")
        lab.mostrarLaberinto()
        print("\n")

    nombreHeur = menuH(lab)

    if nombreHeur is not None:
        menu(lab,nombreHeur)


if __name__ == "__main__":
    main()


