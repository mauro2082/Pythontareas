#Definir una clase en python



class Coche:
    
    
    #atributos o propiedades
    #datos caracteristicos de los objetos
    
    color ="Rojo"
    marca= "Ferrari"
    modelo= 2020
    plazas= 2
    velocidad=500
    
    
    soy_publico = "Hola soy un atributo Publico"
    
    __soy_privado = "Hola soy un atributo privado"
    
    
    
    def __init__(self, color, modelo, velocidad, marca):
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.marca = marca

        
    def getsoyPrivado(self):
        return self.__soy_privado    
    
    # metodos (son acciones del objeto)
    
    def acelerar(self):
        self.velocidad +=1
        
    def frenar(self):
        self.velocidad -=1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo=modelo
    
    def getModelo(self):
        return self.modelo
    
    def getMarca(self):
        return self.marca
    
    def getInfo(self):
        info = "-------- Informacion del Coche---------"
        info += "\n Color:" + self.getColor()
        info += "\n Modelo:" + self.getModelo()
        info += "\n Marca:" + self.getMarca()
        info += "\n Velocidad:" + str(self.getVelocidad())
        
        return info

        
    
