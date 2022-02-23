from re import A
from Ficha import *

class Tablero:
    fichas=[Ficha("a",1),Ficha("v",2)]
    tablero=[]
    turno=1

    
    #for obj in fichas:
     #   if(obj.color=="a"):
      #      print (obj.color)
    #Defina aquí los atributos de Tablero
    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self):
        self.tablero=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase

    #defina aquí los métodos de Tablero
    def turnos(self):
        if(self.turno%2==0):
            return 0
        else:
            return 1

    def dibujar_tablero(self):
        print(" %c | %c | %c " % (self.tablero[0],self.tablero[1],self.tablero[2]))
        print("---+---+---")
        print(" %c | %c | %c " % (self.tablero[3],self.tablero[4],self.tablero[5]))
        print("---+---+---")
        print(" %c | %c | %c " % (self.tablero[6],self.tablero[7],self.tablero[8]))


    def colocar_ficha(self):
        while(True):
            num=self.turnos()
            posicion= self.fichas[num].avanzar()
            poReal=self.verificador(posicion,num)
            if posicion>=0 or posicion<=9:
                if self.tablero[poReal]==" ":
                    self.tablero[poReal]=self.fichas[num].color
                    self.dibujar_tablero()
                    self.turno=self.turno+1
    

    def verificador(self,posicion,turno):
        for i in self.tablero:
            if (self.fichas[turno].color==self.tablero[i]):
                self.tablero.pop(i)
                a=posicion+i
                if(a==9):
                    return a
                if(a>9):
                    return a-9
        return posicion



                



    





    #recuerde que el primer parámetro de cada método es siempre self