import os, time
def delay():
    time.sleep(1)
    #################
def limpiar():
    ###########
    os.system("cls")
def tiempo_espera():
    time.sleep(1)

#.append() para agregar un elemento al final de una lista
libros = []

def agregar_libro():
    limpiar()





    while True:
        titulo = input("ingrese titulo: ")
        duplicado = False
        for libro in libros:
            if libro["titulo"].lower() == titulo.lower():
                duplicado= True

        if duplicado == True:
            print("Titulo ya Existente")
            continue
        else:
            break




    autor = input("ingrese autor: ")
    ####################
    numero_id = len(libros) + 1
    libroplus = {"numero" : numero_id ,"titulo": titulo, "autor": autor, "estado": "disponible" }
    #####################
    libros.append(libroplus)
    print(f"\nLibro: '{titulo}' agregado!!!\n")
        


def mostrar_libros():
    limpiar()
    print("\n   ================ LISTA DE LIBROS ================  \n")
    for libro in libros:
         
         ############
        if libro['estado'] == "disponible":
            estado = "Disponible"
        else:
            estado = "Prestado"
        print(f"Libro N°{libro['numero']}\n\nTitulo:  {libro['titulo']}\nAutor:   {libro['autor']}\nEstado:  {estado}")
        print("\n=============================================================\n")
        tiempo_espera()
        ##########

def buscar_libro():
    limpiar()
    estadolibro = input(" ingrese titulo del libro que busca: ")
    encontrado = False
    #for x in libros:
    for libro in libros:
        if libro["titulo"].lower() == estadolibro.lower():
            encontrado = True          
            print("\nlibro disponible!!\n==================")
            print(f"Libro N°{libro['numero']} \n\nTitulo:  {libro['titulo']}\nAutor: {libro['autor']}\nEstado: {libro['estado']} \n")##########################################
            break
    if not encontrado:
        print ("\n!Libro no disponible!!!\n")


def prestar_libro ():
    limpiar()
    prestar = input(" Ingrese titulo del libro que quiere tomar prestado: ")
    encontrado = False 
    for libro in libros:
        if libro["titulo"].lower() == prestar.lower():
            encontrado = True
            if libro["estado"] == "prestado":
                print(f"\nel libro: '{libro["titulo"]}' ya fue prestado!!!\n")
            else:
                libro["estado"] = "prestado"
                print(f"\nlibro: '{libro["titulo"]}' prestado con exito!!!\n")
            break
    if not encontrado:
        print(f"\n!El libro '{prestar}' no esta en el sistema!!!\n")


def devolver_libro ():
    limpiar()
    devolver = input(" ingrese titulo del libro que quiere regresar: ")
    encontrado = False
    for libro in libros:
        if libro["titulo"].lower() == devolver.lower():
            encontrado = True
            if libro["estado"] == "disponible":
                print(f"\nel libro: '{libro["titulo"]}' el libro fue devuelto anteriormente!!!\n")
            elif libro["estado"] == "prestado":
                libro["estado"] = "disponible"
                print("\nlibro devuelto exitosamente!!!\n")
            break
    if not encontrado:
        print(f"\n!El libro '{devolver}' que desea devolver no esta en el sistema!!!\n")


def eliminar_libro ():
    limpiar()
    eliminar = input("ingrese titulo del libro que desea eliminar: ")
    encontrado = False
    for libro in libros:
        
        if libro["titulo"].lower() == eliminar.lower():
            
            encontrado = True
            libros.remove(libro)
            ####################
            numero_id = 1  

            for libro in libros:
                libro["numero"] = numero_id 
                numero_id = numero_id + 1
                #########################
            print(f"\nEl libro: '{eliminar}' a sido eliminado del sistema!!!\n")
            break
    if not encontrado:
        print("\n!El libro que desea eliminar no esta en el sistema!!!\n")


def modificar_libro():
    limpiar()
    modificar = input(" Ingrese titulo del libro que desea modificar: ")
    encontrado =  False
    for libro in libros:
        if libro["titulo"].lower() == modificar.lower():
            encontrado = True
            nuevo_titulo = input("\n Ingrese nuevo titulo: ")
            nuevo_autor = input(" Ingrese nuevo autor: ")
            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor
            print("\nLibro modificado con exito!!!\n")
            break
    if not encontrado:
        print("\n!El libro que desea modificar no existe\n")


def mostrar_estadisticas():
    limpiar()

    total_libros = len(libros)
    disponibles = 0
    prestados = 0

    for libro in libros:
        if libro["estado"] == "disponible":
            disponibles+=1
        elif libro["estado"] == "prestado":
            prestados+=1
                                                          
    print(f"· Cantidad total de libros:   {total_libros}\n==================================")
    print(f"· Libros disponibles: {disponibles}")
    print(f"· Libros prestados:   {prestados}\n")



    







