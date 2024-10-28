#importar modulo


import sqlite3


#crear una variable de conexion 


connection = sqlite3.connect('pruebas.db')

#crear tabla


# crear cursor para realizar consultas y crear tablas

cursor = connection.cursor()   

#tabla

cursor.execute("""CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               Title varchar(225),
               Description text, 
               price int(255)
               )""")


#PARA GUARDAR CAMBIOS DEBO HACER UN COMMIT

connection.commit()


#insertar datos a nuestra tabla


# cursor.execute("INSERT INTO products VALUES(null,'first product','description of product', 5000) ")
# connection.commit()



#borrar resgistros de una tabla 


cursor.execute("DELETE FROM products;")
connection.commit()



#ingresar varos registros a la vez

productos = [
    ("macbook", "año 2012", 800),
    ("PS5", "año 2023", 15000),
    ("PS4", "año 2018", 600),
] 

cursor.executemany("INSERT INTO products VALUES (null, ?, ?, ?)", productos)
connection.commit()

#listar datos de una tabla 


cursor.execute("SELECT * FROM products where price >1000;")

products = cursor.fetchall()

for product in products:
    print(product)




# cerrar conexion 

connection.close()