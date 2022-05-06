class Base1:
    def __init__(self, a):
        print('Base1 init')
        self.a = a

    def some_method(self):
        print(f'a: {self.a}')


class Base2:
    def __init__(self, b):
        print('Base2 init')
        self.b = b

    def other_method(self):
        print(f'a: {self.a}')


class Derived(Base1, Base2):
    def __init__(self, a, b, c):
        Base1.__init__(self, a)
        Base2.__init__(self, b)
        print('Derived init')
        self.c = c

    def another_method(self):
        self.some_method()
        print(f'b: {self.c}')


d = Derived(1, 2, 3)
d.some_method()
d.other_method()
d.another_method()
