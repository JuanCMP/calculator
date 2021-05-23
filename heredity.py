
class rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class cuadrado(rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado ,lado)


if __name__ == '__main__':
    Rectangulo = rectangulo(base = 5, altura = 4)
    print(Rectangulo.area())
    Cuadrado = cuadrado(lado = 5)
    print(Cuadrado.area())
    