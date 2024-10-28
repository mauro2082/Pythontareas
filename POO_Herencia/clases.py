#herencia. capacidad de compartir atributos y metodos entre clases padre a clases hijas


class persona():
    
    #atributos
    
    # nombre
    # apellidos
    # altura
    # edad
    
    
    #metodos
    
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apelidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apelidos = apellidos
        
    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad
        
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

class Informatico(persona):
    
    #atributos
        
    # lenguajes
    # experiencia
    
    
    #metodos
    
    
    def __init__(self):
        self.lenguajes = "THML, CSS, JS, REACT, PYTHON"
        self.experiencia = 5
        
    def getLenguajes(self):
        return self.lenguajes
    
    def setAprender(self, lenguaje):
        self.lenguajes =+  lenguaje
        return self.lenguajes
        
    
    
    


