# -*- coding: utf-8 -*-
print("Trabajo realizado por Gustavo Adrian Avila Zapata \nRAM: 4096")
print("Modificacion para la Tarea de APS por Serapio Hernández")
print("\n'Administracion de memoria RAM'\n")
print("¿Que tecnica de gestion de memoria desea utilizar?\n"
      "1.- Estatico\n"
      "2.- Dinamico\n"
      "3.- Paginacion\n"
      "4.- Segmentacion\n"
      "5.- Salir")

metodo = int(input("Eleccion: "))

def menu(metodo):
    if metodo == 1: 
       memoriasig = 4096
       metodo1(memoriasig)
    elif metodo == 2: 
       memoriasig = 4096
       metodo2(memoriasig)
    elif metodo == 3:
        metodo3()
    elif metodo == 4: 
        memoriasig = 4096
        metodo4(memoriasig)
    elif metodo == 5:  
        exit("Saliendo")

def metodo1(memoriasig):
    print('Metodo Estatico')
    listaestatica = []
    listaestaticap = []
    sumaestatica = 0
    a = 0
    numestatica = int(input("Particiones? "))

    while numestatica > 0:
        segmentomemoria = int(input("Particion:"))
        if segmentomemoria <= memoriasig:
            if 4098 > sumaestatica:
                listaestatica.append(segmentomemoria)
                sumaestatica = sum(listaestatica)
                memoriasist = memoriasig - segmentomemoria
                tamañoproceso = int(input("Tamaño Proceso:"))
                if listaestatica[a] >= tamañoproceso:
                    listaestaticap.append(tamañoproceso)
                    a = a + 1
                    numestatica = numestatica - 1
                else:
                    print("Memoria insuficiente")
                    numestatica = numestatica - 1
            else:
                print("No hay memoria")
        else:
            print("No hay memoria")
            break
    print("lista final:", listaestaticap)

def metodo2(memoriasig):

    print('Metodo Dinamico')
    memdispdin = 4096
    while 0 <= 4096:
        if memdispdin > 0:
            vardinamico = int(input("Proceso? "))
            if vardinamico <= memoriasig:
                nuevamem = memdispdin - vardinamico
                print("Memoria Sobrante: ", nuevamem)
                memdispdin = memdispdin - vardinamico
            else:
                print("Proceso excedido")
        else:
            print("Memoria Rebasada")
            break

def metodo3():
    print('Metodo Paginacion')
    tam_pag = int(input("Tamaño de las paginas:"))
    paginas = 4096 / tam_pag
    while paginas >= 0:
        paginaproceso = int(input("Tamaño Proceso:"))
        pagnuev = paginaproceso / tam_pag
        paginas = paginas - pagnuev
        print("\nMemoria Restantes",tam_pag,"(por pagina)","restantes: ", int(paginas))
        print("En memoria RAM: ",paginas * tam_pag)
        print("Paginas ocupadas por el proceso: ", paginaproceso / tam_pag)
      
def metodo4(memoriasig):
    print('Metodo Segmentacion')
    while memoriasig >= 0:
        process = int(input("Proceso:"))
        if process <= memoriasig:
            print("Seg. Pila: ", process * .1)
            print("Seg. de Codigo: ", process * .2)
            print("Seg. de Datos: ", process * .7)
            memoriasig = memoriasig - process
        else:
            print("Tamaño insuficiente")

menu(metodo)

