'''class midecorador(object):
    def __init__(self, func):
        print('He construido la clase')
        func()
    def __call__(self):
        print('Soy una clase llamada mediante call')

@midecorador
def hablar():
    print('Hola soy la funcion hablar')'''

# Pero si nosotros queremos que la misma no sea llamada
# automáticamente debemos almacenarla en el constructor y llamarla en el call.

'''class midecoradorI(object):
    def __init__(self, func):
        print('He constrido una clase')
        self.func = func
    def __call__(self):
        print('Soy otra clase llamada mediante call')
        self.func()
@midecoradorI
def cantar():
    print('Soy la funcion de cantar')
cantar()'''

# Esta es otra opcion en la que se puede usar decoradores
class midecoradorIII(object):
    def __init__(self, func):
        print('Construccion de una clase')
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Clase llamada mediante call')
        self.func(*args, **kwargs)

@midecoradorIII
def dormir(mensaje):
    print(mensaje)
dormir('Esta es una funcion de dormir')


if __name__=='__main__':
    hablar()