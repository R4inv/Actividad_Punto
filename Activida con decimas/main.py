from functions import *
limpiar()

while True:
    try:
        
            print("===== BIBLIOTECA =====\n1. Agregar libro\n2. Mostrar libros\n3. Buscar libro\n4. Prestar libro\n5. Devolver libro\n6. Eliminar libro\n7. Modificar libro\n8. Mostrar estadísticas\n9. Salir")

            opciones = int(input(""))

            if opciones == 1 :
                agregar_libro()
            elif opciones == 2 :
                mostrar_libros()
            elif opciones == 3:
                buscar_libro()
            elif opciones == 4:
                prestar_libro()
            elif opciones == 5:
                devolver_libro()
            elif opciones == 6:
                eliminar_libro()
            elif opciones == 7:
                modificar_libro()
            elif opciones == 8:
                mostrar_estadisticas()
            elif opciones == 9:
                break
            else:
                print("Opcion inválida!")
    except:
        print("los valores ingresados deben ser numericos\n\n")
        continue