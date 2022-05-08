from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        raise NotImplementedError(self)

    @abstractmethod
    def walk(self):
        pass


class Cat(IAnimal):
    def sound(self):
        print('Nyaaa')

    def walk(self):
        super(Cat, self).walk()
        print('suta suta')


class Dog():
    def sound(self):
        print('Wow')

    def walk(self):
        print('teku teku')


try:
    IAnimal.register(Dog)
except AttributeError:
    print('No implementation')

if __name__ == "__main__":
    assert issubclass(Cat().__class__, IAnimal)
    assert isinstance(Cat(), IAnimal)
    Cat().sound()
    Cat().walk()

    assert issubclass(Dog().__class__, IAnimal)
    assert isinstance(Dog(), IAnimal)
    Dog().sound()
    Dog().walk()
