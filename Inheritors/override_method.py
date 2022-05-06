class Base:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def some_method(self):
        print(f'a: {self.num1} b: {self.num2}')

    def calc_sum(self):
        return self.num1 + self.num2


class Derived(Base):
    def __init__(self, num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3

    def another_method(self):
        self.some_method()
        self.sum = Base.calc_sum(self)
        print(f'sum: {self.sum}, num3: {self.num3}')

    def calc_sum(self):
        tmp = Base.calc_sum(self)
        return tmp + self.num3


d = Derived(1, 2, 3)
d.another_method()
print(f'{d.calc_sum()}')
