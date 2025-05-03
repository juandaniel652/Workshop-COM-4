#¿Para qué es *args y **kwargs?: 
# *args permite pasar un número variable de argumentos posicionales a la función decorada. (1, 2, 3, ...)
# **kwargs permite pasar un número variable de argumentos nombrados (clave-valor) a la función decorada. (edad=25, nombre="Juan", ...)

def decorador(funcion):
   
    def mi_fruta(*args, **kwargs) :

        print("Inicio del recorrido de frutas:")
        funcion()
        print("Fin del recorrido de frutas.\n")

    return mi_fruta


@decorador
def recorrer_frutas():

    frutas = ["manzana", "banana", "naranja", "pera", "melon"]

    for fruta in frutas:

        print(fruta)


recorrer_frutas()

#Devuelve la función decorada, que a su vez devuelve la función original con el recorrido de frutas,
#pero con el mensaje de inicio y fin del recorrido.