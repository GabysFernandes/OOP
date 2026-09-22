from abc import ABC, abstractmethod


class IFly(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class IJump(ABC):
    @abstractmethod
    def jump(self):
        pass


class IClimb(ABC):
    @abstractmethod
    def climb(self):
        pass


class ISling(ABC):
    @abstractmethod
    def sling(self):
        pass