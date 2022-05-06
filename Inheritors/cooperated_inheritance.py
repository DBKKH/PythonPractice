class B0:
    def __init__(self):
        print('B0 init')


class B1(B0):
    def __init__(self, a, **kwargs):
        print('B1 init')
        super().__init__(**kwargs)
        self.a = a


class B2(B0):
    def __init__(self, b, **kwargs):
        print('B2 init')
        super().__init__(**kwargs)
        self.b = b


class D(B1, B2):
    def __init__(self, c, **kwargs):
        print('D init')
        super().__init__(**kwargs)
        self.c = c


d = D(a=0, b=1, c=2)
print(f'a: {d.a}, b: {d.b}, c: {d.c}')
