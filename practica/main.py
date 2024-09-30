

#   funciones para cada tarea 

# agregar tarea



tareas={
}

def agregartarea(tarea):
   clave_tarea = len(tareas) + 1
   tareas.update({
        clave_tarea: {
            "tarea": tarea,
            "Cumplida": False
        }
    })

#  listar tarea

def listartarea():
    largo = len(tareas)
    if largo != 0:
        for clave, tarea in tareas.items():
            print(f"* {clave}: {tarea} ")
    else:
        print("No hay tareas por mostrar") 
    
    
#  Marcar tarea como completada

def tareaCumplida(dato):
    # Recorrer el diccionario usando sus claves
    for clave_tarea, info in tareas.items():
        # Si la tarea coincide con 'dato'
        if clave_tarea == dato:
            # Marcar la tarea como cumplida
            tareas[clave_tarea]['Cumplida'] = True
            print(f"Tarea '{dato}' marcada como cumplida.")
            return
    
    print(f"Tarea '{dato}' no encontrada.")


print("\n")
print("******************SISTEMA DE ASIGNACION DE TAREAS VB1********************\n\n")
print("              Por favor seleccionar del menu la opcion deseada: \n\n")  



def menu():
    seleccion=10
    while seleccion < 1 or seleccion  > 4:
         print("POR FAVOR SELECCIONE LA OPCION DEL SIGUIENTE MENU: \n")
         print("1 Para Agregar tarea. ")
         print("2 Para Listar tarea. ")
         print("3 Para marcar tarea como completa. ")
         print("4 Para Salir del Menu. \n")
         seleccion = int(input("Ingrese aca el numero del 1 al 4: \n\n"))
    if seleccion == 1:
        print("haz Seleccionado la Opcion Agregar Tarea:  \n")
        print("____________________________________________")
        asignar= input("Por favor indique la tarea realizar:")
        agregartarea(asignar)
        print(f" la Tarea: {asignar}fue asignada exitosamente")
        menu()
    elif seleccion == 2:
        print("Has seleccionado la opción Listar Tareas.\n")
        listartarea()
        menu()
    elif seleccion == 3:
        print("Has seleccionado la opción Marcar tarea como completa.\n")
        print("Por favor seleccionar la Tarea a marcar como pumlida")
        listartarea()
        
        largo = len(tareas)
        while largo <= seleccion:
            seleccion = int(input("Por favor selecione de la lista la tarea a completar: "))
            tareaCumplida(seleccion)
            seleccion=-1000
            menu()
    elif seleccion == 4:
        print("Saliendo del menú...")


    #iniciar la funcion

menu()
        


         







    

    
    