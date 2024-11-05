# Proyecto Agenda 
from users  import action

hazEl = action.Actions()

print("""
*****************************************************************      
|                 Bienvenido al Sistema de Notas                |
|                            Personales                         |
*****************************************************************  
      
Acciones disponibles:
   
      1. Registro
      2. Login
      
      """)
accion = -1
while accion < 0 or accion > 2: 
    accion = int(input("\n Por favor Selecciona una opcion entre 1(Registro) o 2(Login): "))
    if accion == 1:
        print("\n OK, Seleccionaste Registro \n")
        hazEl.RegisUser() 
    elif accion == 2:
        print("\nOk, Por favor identificate \n")
        hazEl.login()
        
       
        


    
    