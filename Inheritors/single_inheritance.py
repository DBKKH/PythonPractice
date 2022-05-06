class Base:
    def __init__(self, a):
        print('Base init')
        self.a = a

    def some_method(self):
        print(f'a: {self.a}')


class Derived(Base):
    def __init__(self, a, b):
        print('Derived init')
        super().__init__(a)
        self.b = b

    def another_method(self):
        # self.some_method()
        print(f'b: {self.b}')


d = Derived(1, 2)
d.some_method()
d.another_method()
