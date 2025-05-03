#Decoradores en Python

#INTEGRANTES: 
#-	AGÜERO GERSON
#-	DOMINGUEZ JUAN
#
#PREGUNTA RETÓRICA: 
#¿Qué es un decorador en Python y para qué se utiliza comúnmente?
#
#Los decoradores en Python son básicamente funcionalidades extras que se pueden agregar a funciones que ya existen para poder así “decorarlas”.
#Toma una función como entrada, le agrega una funcionalidad extra y devuelve como salida la función modificada. 
#¿Qué ventajas ofrece?: No modifica el código original de la función, logrando que, al querer añadir nuevas funcionalidades, no afecte o “rompa” lo previamente desarrollado.
#
#MINI EVALUACIÓN
#¿CÓMO SE APLICA A UNA FUNCIÓN?: 
#
#1. Ya definida la función original: 
#1 – Se crea otra función que recibe como argumento la función original.
#2 – Dentro de esta función que es el decorador se crea otra función, dentro de la cual es posible “envolver” la función original, de esa manera añadirle nuevas funcionalidades.
#3 – Se retorna la función que está dentro de la que funciona como decorador.
#
#¿Qué función interna suele tener un decorador?: 
# Al ser una función anidada (una dentro de la otra) es posible “encapsular” la función para su modificación.  Esta función recibe como argumentos *args y **kwargs, las cuales le permiten recibir cualquier tipo de función con distintos valores.
#
#Reflexión individual: 
#Algunos de los que son utilizados son @staticmethod o @classmethod los cuales añaden funcionalidades a métodos que influyen en sus acciones. Sí, es muy apropiado para proyectos propios, de esa manera hacerlo escalable.
