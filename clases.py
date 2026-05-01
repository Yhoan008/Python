#CLASES Y POO



class Animal:
    def __init__(self):                 #Esta es la funcion constructor (Siempre asi se declara)
        print("Instancia creada")

    def correr(self):
        print("El animal corre")

    def comer(self):
        print("El animal esta comiendo")


#Asi aplicamos herencia
class Conejo(Animal):
    pass 
    def __init__(self,alto,peso):
        self.alto = alto
        self.peso = peso
        print(f"El conejo pesa {peso}kg y de alto {alto}cm")
    
    def __saltar(self):             #Esto es una clase privada
        print("Estoy saltando")     #Solo puedo acceder _Clase__Metodo()
    



#conejo1 = Conejo(12,30)
#conejo1.correr()

#conejo1._Conejo__saltar()   #Asi accedo al metodo




#METODOS ESPECIALES DE OBJETOS

#__new__(cls, args)
#Método exclusivo de las clases de nuevo estilo que se ejecuta antes que
#__init__ y que se encarga de construir y devolver el objeto en sí.


#__del__(self)
#Método llamado cuando el objeto va a ser borrado. También llamado
#destructor


#__str__(self)
#Método llamado para crear una cadena de texto que represente a nuestro objeto.


#__cmp__(self, otro)
#Método llamado cuando se utilizan los operadores de comparación
#para comprobar si nuestro objeto es menor, mayor o igual al objeto
#pasado como parámetro.


#__len__(self)
#Método llamado para comprobar la longitud del objeto.



#RECUERDA QUE TAMBIEN APLICAN METODOS DE CADENAS, LISTAS, DICCIONARIOS