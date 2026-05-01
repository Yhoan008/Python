#PROGRAMACION FUNCIONAL


#Funciones de orden superior, son funciones contenidas en otra funcion


def saludar(lang):
    def saludar_es():
        print ("Hola")

    def saludar_en():
        print ("Hi")

    def saludar_fr():
        print ("Salut")

    lang_func = {"es": saludar_es,
                "en": saludar_en,
                "fr": saludar_fr}

    return lang_func[lang]

saludar("en")()


#Aca almacenamos las funciones en un diccionario y se usa doble llamado de funcion
#Aunque tambien funciona asi

f = saludar("es")
f()