
import datetime
import hashlib  # permite cifrar las contraseñas en la base de datos
#print(connection)

from conexBD import CBD

connection = CBD()
cursor = connection.get_cursor()

class users:
    
    def __init__(self, nombre, apellido, email, password):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.password=password
        
        
    def registrar(self):
        fecha=datetime.datetime.now()
        
        #cifrar contraseña
        
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO users VALUES(null, %s,%s,%s,%s,%s)"
        usuario=(self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        
        cursor.execute(sql, usuario)
        connection.commit()
        
        
        print("Filas insertadas:", cursor.rowcount)
        connection.close()
        return self
       
        
    def identificar(self):
        print("Identificado")