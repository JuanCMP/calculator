def decorator(func):
    def new_function():
        print('Perro dice')
        func()
    return new_function

@decorator
def saluda():
    print('Guauu!')

def despide():
    print('Chau!')
saluda()
despide()
