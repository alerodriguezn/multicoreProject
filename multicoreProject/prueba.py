from multiprocessing import Pool
lista = []

def funcion(x):
    global lista
    lista.append(x)
    return lista




with Pool() as p:

    lista_contenido = p.map(funcion, [1,2,3,4,5,6,7,8,9])# Aqui se divide la lista en 3 procesos
    print (lista_contenido)


