def decorador(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs) #Esa linea logra llamar a los atributos de la funcion original
        if resultado == True:
            return "Acceso permitido"
        else:
            return "Acceso denegado"
    return wrapper

@decorador
def acceso(): 
    is_admin = True
    return is_admin

acceso()