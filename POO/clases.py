#Definir una clase en python



class Coche:
    
    
    #atributos o propiedades
    #datos caracteristicos de los objetos
    
    color ="Rojo"
    marca= "Ferrari"
    modelo= 2020
    plazas= 2
    velocidad=500
    
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
    
# instanciar la clase

