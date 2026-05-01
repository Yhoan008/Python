#Esta clase tiene una variable privada 
#Para modificarla usamos el tipico Get Set

#Pero object y property que son?

class Fecha(object):
    def __init__(self):
        self.__dia = 28
    
    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print ("Error")
        
    dia = property(getDia, setDia)



mi_fecha = Fecha()
mi_fecha.getDia()
mi_fecha.dia = 33







#funciones de orden superior
