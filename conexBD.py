import mysql.connector

class CBD:
    
    def __init__(self):
        # Crea y almacena la conexión y el cursor al inicializar la clase
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Agenda",
            port=3306  # Cambia el puerto si es necesario
        )
        self.cursor = self.connection.cursor(buffered=True)
    
    def get_cursor(self):
        # Método para acceder al cursor desde otras partes del código
        return self.cursor
    
    def commit(self):
        # Método para realizar commit después de una transacción
        self.connection.commit()
    
    def close(self):
        # Método para cerrar la conexión
        self.cursor.close()
        self.connection.close()
