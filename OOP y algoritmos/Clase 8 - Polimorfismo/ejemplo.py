class SuperClass:
    def __init__(self):
        pass

    def action1(self):
        print('Soy una acción de la superclase')


class SubClass(SuperClass):
    def __init__(self):
        super().__init__()

    def action1(self):
        print('Soy una acción modificada para la subclase')


if __name__ == '__main__':
    superclass = SuperClass()
    subclass = SubClass()

    superclass.action1()
    subclass.action1()
