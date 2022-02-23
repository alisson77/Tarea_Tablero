from Dado import *

class Ficha:
    color = ""
    posicion = 0
    turno=0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(4)
    
    
    def __init__(self, color,turno):
        self.color = color
        self.turno=turno
        self.posicion = 0
        
    
    def avanzar(self):
        #aquí se vuelve claro por qué necesitamos un dado
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.posicion)
        return self.posicion