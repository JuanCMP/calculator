class persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f'Mi nombre es {self.nombre}')
    def desplaza(self):
        print('Me estoy desplazando a pie')

class ciclista(persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def desplaza(self):
        print('Me estoy movilizando en mi bici')

def main():
    Persona = persona('Camilo')
    Persona.desplaza()
    Ciclista = ciclista('Juan')
    Ciclista.desplaza()


if __name__ == '__main__':
    main()

        

