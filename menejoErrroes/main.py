


try:
    nombre = input("Ingresa tu nombre: ")
    if len(nombre) > 1:
        usuario= "Bienvenido: "+nombre
    print(usuario)
except:
    print("Ha ocurrido un error, ingresa un nombre")
else:
    print("Usuario creado con exito")
finally:
    print("Fin de la iteracion")

