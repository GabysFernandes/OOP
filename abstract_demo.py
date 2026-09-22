from abc import ABC, abstractmethod
from interfaces import IFly, IJump, IClimb 


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} makes the sound {self.make_sound()}"

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal, IJump):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        raise NotImplementedError(
            "Dog.jump() has not been implemented yet."
        )

    def make_sound(self):
        return "Woof Woof Ow"


class Wolf(Animal, IJump):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        raise NotImplementedError(
            "Wolf.jump() has not been implemented yet."
        )

    def make_sound(self):
        return "AAAAUUUUUUUUU"


class Cat(Animal, IJump, IClimb):
    def __init__(self, name):
        super().__init__(name)

    def climb(self):
        raise NotImplementedError(
            "Cat.climb() has not been implemented yet."
        )

    def jump(self):
        return "Boing Boing Boing"

    def make_sound(self):
        return "Miaow Miaow ow"


class LandBird(Animal, IJump):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        return "Hop Hop Hop"

    def make_sound(self):
        return "Squawk squawk"


class FlyBird(Animal, IFly, IJump):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        raise NotImplementedError(
            "FlyBird.fly() has not been implemented yet."
        )

    def jump(self):
        return "Hop Hop Hop"

    def land(self):
        raise NotImplementedError(
            "FlyBird.land() has not been implemented yet."
        )

    def make_sound(self):
        return "Chirp chirp chirp"