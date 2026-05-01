# INPUTS 

#Para pedir informacion al usuario 

#nombre = input("Cual es su nombre, maestro: ")

#print(f'Hola {nombre}')

caracter = "d"

numero = caracter*5

#print(numero)     #ddddd


#number = float(input("Ingrese un numero: "))  #Como devuelve entero convertimos a int 

#print(number*2)

#Con type podemos ver el tipo de dato con el que estamos trabajando
#print (type(number))


#Para la declaracion de funciones se hace con def

def miPrimeraFuncion(parametro1,parametro2):
    print ("El parametro 1 es: ",parametro1)
    print ("El parametro 2 es: ",parametro2)
    
#miPrimeraFuncion("jorgue","nitales")



#Ahora while e if else elif

"""
salir = False
while not salir:
    sale = input(">")
    if sale == "1":
        salir = True
    else:
        print(sale)

"""


#Bucles for
"""
secuencia = [1,2,3,5,8]

for elemento in secuencia:
    print(elemento)

"""



def funcion2(texto,number):
    print (texto*number)

#funcion2("goetia",2)





#Podemos devolver mas de un valor en forma de tupla

def funcion3(x,y):
    return x+y,x-y

a,b = funcion3(4,2)

print (a,b)