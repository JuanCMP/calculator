def decorador(func):
    def nueva_funcion(self, mensaje):
        print('Perro dice...')
        func(self, mensaje)
    return nueva_funcion

class perro(object):
    def __init__(self, nombre):
        self.nombre = nombre
    @decorador
    def saluda(self, mensaje):
        self.mensaje = mensaje
        print(mensaje)
        print('Guauu!')

maty = perro('maty')
maty.saluda('Uso Puppy linux!')


def decorador(func):
    def nueva_funcion(self, parametro1):
        print ("Perro dice:")
        func(self, parametro1) 
    return nueva_funcion 

class perro(object):
    def __init__(self, nombre): 
        self.nombre = nombre 
    @decorador 
    def saluda(self, mensaje): 
        self.mensaje = mensaje 
        print(f'Soy {self.nombre}, mucho gusto')
        print(mensaje)
        print("Guau!") 
    @decorador
    def ordeno(self, orden):
        self.orden = orden
        print(orden)
        print("La pata, la pata afgsad! Guau!")
joe = perro('Joe')
joe.saluda('Uso Puppy Linux!')
joe.ordeno('Doy la pata')

