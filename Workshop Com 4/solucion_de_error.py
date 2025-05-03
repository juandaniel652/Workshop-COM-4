#Código erróneo

#def decorator(func): 
#    print("Decorating...") 
#    return func 
# 
#@decorator 
#def greet(): 
#    print("Hi!") 
#greet()

#Código corregido	

def decorator(func): 

    def wrapper(*args, **kwargs) :
        
        print("Decorating...")
        func() 

    return wrapper
 
@decorator 
def greet(): 
    print("Hi!") 
greet()