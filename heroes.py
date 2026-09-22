from abc import ABC
from interfaces import IFly
from interfaces import ISling


class Being(ABC):
    pass


class SuperHero(Being):
    pass


class HumanHero(SuperHero):
    pass



class Batman(HumanHero, IFly):
    def fly(self):
        print("I am flying with my bat wings")

    def land(self):
        print("I am landing with my bat wings")


class SpiderMan(HumanHero, ISling):
    def sling(self):
        print("I am sling with my web")

    def land(self):
        print("I am climbing with my web")