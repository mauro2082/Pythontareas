import users.users as model
from conexBD import CBD

connection = CBD()
cursor = connection.get_cursor()


class Actions:
    
    
    def RegisUser(self):
        
        
        nombre = input("Por favor ingresa tu nombre: ")
        apellido = input("Por favor ingresa tu apellido: ")
        email = input("Por favor ingresa tu correo: ")
        
        sql_verificar = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql_verificar, (email,))
        
        while cursor.fetchone() is not None:
            print("Este correo ya esta registrado intenta con otro")
            email = input("Por favor ingresa tu correo: ")
            
        password = "1"
        password2 = "2"
        
        while password != password2:
            password = input("Por favor ingresa tu contraseña: ")
            password2 = input("Por favor ingresa de nuevo tu contraseña: ")
            if password != password2:
                print("Las contraseñas no coinciden, intentalo de nuevo")
        
        usuario = model.users(nombre, apellido, email, password)
        registro = usuario.registrar()
        
        if cursor.fetchone :
            print(f"\nRegistro exitoso, Bienvenido {registro.nombre} feliz dia")
        else:
            print("Usuario no registrado...")
        
    def login(self):
         
         email= input("\nIngresa tu email: ")
         password= input("\nIngresa tu Contraseña: \n")
         
         sql_login = "SELECT * FROM users WHERE email = %s AND password = %s "
         cursor.execute(sql_login, (email, password))
         
         if cursor.fetchone() is not None:
            print("Bienvenido al sistema ")
         else:
             print("Contraseña o usuario incorrecto. Intentalo de nuevo")
            
         
         
        