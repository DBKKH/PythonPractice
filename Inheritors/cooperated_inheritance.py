class Base0:
    def __init__(self):
        print('B0 init')


class Base1(Base0):
    def __init__(self, a, **kwargs):
        print('B1 init')
        super().__init__(**kwargs)
        self.a = a


class Base2(Base0):
    def __init__(self, b, **kwargs):
        print('B2 init')
        super().__init__(**kwargs)
        self.b = b


class Derived(Base1, Base2):
    def __init__(self, c, **kwargs):
        print('Derived init')
        super().__init__(**kwargs)
        self.c = c


d = Derived(a=0, b=1, c=2)
print(f'a: {d.a}, b: {d.b}, c: {d.c}')
