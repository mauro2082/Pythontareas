import mysql.connector


# conexion a la base de datos



database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)


#verificar la conexion 

# print(database)

#crear cursos para realizar consultas


cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
# cursor.execute("SHOW DATABASES")


for bd in cursor:
    print(bd)
    
#crear tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculos PRIMARY KEY(id) 
)              
""")


cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
    
    
    #insertar registros en las tablas
    
    
    # cursor.execute(" INSERT INTO vehiculos VALUES(null, 'OPEL','ASTRA', 18500)")
    
    
    carros =[
        ('Mazda','2', 1000),
        ('Chevrolet','Spark', 1200),
        ('Renaulth','twingo', 500)
    ]
    
    # cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", carros)
    
    
    database.commit()