import os, time
def delay():
    time.sleep(1)
def limpiar():
    os.system("cls")

#.append() para agregar un elemento al final de una lista
libros = []

def agregar_libro():
    titulo = input("ingrese titulo: ")
    autor = input("ingrese autor: ")
    libroplus = {"titulo": titulo, "autor": autor, "estado": "disponible" }
    if libroplus in libros:
        print("!No se permiten libros repetidos")
    else:
        libros.append(libroplus)
        print(f"libro: {titulo} agregado")


def mostrar_libros():
    for libro in libros:
        print(libro)


def buscar_libro():
    estadolibro = input(" ingrese titulo del libro que busca: ")
    encontrado = False
    #for x in libros:
    for libro in libros:
        if libro["titulo"].lower() == estadolibro.lower():
            encontrado = True
            print("libro disponible")
            print(libro)
            break
    if not encontrado:
        print ("!Libro no disponible")


def prestar_libro ():
    prestar = input(" ingrese titulo del libro que quiere tomar prestado: ")
    encontrado = False 
    for libro in libros:
        if libro["titulo"].lower() == prestar.lower():
            encontrado = True
            if libro["estado"] == "prestado":
                print(f"el libro: {libro["titulo"]} ya fue prestado")
            else:
                libro["estado"] = "prestado"
                print(f"libro: {libro["titulo"]} prestado con exito")
            break
    if not encontrado:
        print(f"!El libro {prestar} no esta en el sistema")


def devolver_libro ():
    devolver = input(" ingrese titulo del libro que quiere regresar: ")
    encontrado = False
    for libro in libros:
        if libro["titulo"].lower() == devolver.lower():
            encontrado = True
            if libro["estado"] == "disponible":
                print(f"el libro: {libro["titulo"]} el libro fue devuelto anteriormente")
            elif libro["estado"] == "prestado":
                libro["estado"] = "disponible"
                print("libro devuelto exitosamente")
            break
    if not encontrado:
        print(f"!El libro {devolver} que desea devolver no esta en el sistema")


def eliminar_libro ():
    eliminar = input("ingrese titulo del libro que desea eliminar: ")
    encontrado = False
    for libro in libros:
        print(f"L1:{libro}")
        if libro["titulo"].lower() == eliminar.lower():
            print(f"L2:{libro}")
            encontrado = True
            libros.remove(libro)
            print(f"el libro: {libro["titulo"]} a sido eliminado del sistema")
            break
    if not encontrado:
        print("!El libro que desea eliminar no esta en el sistema")


def modificar_libro():
    modificar = input(" ingrese titulo del libro que desea modificar: ")
    encontrado =  False
    for libro in libros:
        if libro["titulo"].lower() == modificar.lower():
            encontrado = True
            nuevo_titulo = input(" ingrese nuevo titulo: ")
            nuevo_autor = input(" ingrese nuevo autor: ")
            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor
            print("libro modificado con exito")
        break
    if not encontrado:
        print("!El libro que desea modificar no existe")


def mostrar_estadisticas():

    total_libros = len(libros)
    disponibles = 0
    prestados = 0

    for libro in libros:
        if libro["estado"] == "disponible":
            disponibles+=1
        elif libro["estado"] == "prestado":
            prestados+=1
        
    print(f"· Cantidad total de libros:   {total_libros}")
    print(f"· Cantidad de libros disponibles: {disponibles}")
    print(f"· Cantidad de libros prestados:   {prestados}")



    







