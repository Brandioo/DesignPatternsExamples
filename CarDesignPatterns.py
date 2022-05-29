from __future__ import annotations
from abc import ABC, abstractmethod


class CarCreator(ABC):

    @abstractmethod
    def factory_method(self, production_year):
        pass

    def buy_car(self, production_year) -> Car:
        car = self.factory_method(production_year)
        car.set_taxes()
        return car


class BmwCreator(CarCreator):

    def factory_method(self, production_year) -> Car:
        return Bmw(production_year)


class BenzCreator(CarCreator):

    def factory_method(self, production_year) -> Car:
        return Benz(production_year)


class Car(ABC):

    def __init__(self, production_year: int):
        self.production_year = production_year
        self.tax = None

    @abstractmethod
    def set_taxes(self):
        pass


class Bmw(Car):

    def __init__(self, production_year: int = 2012):
        super().__init__(production_year=production_year)

    def set_taxes(self):
        if self.production_year <= 2015:
            self.tax = 500
        else:
            self.tax = 100


class Benz(Car):

    def __init__(self, production_year: int = 2010):
        super().__init__(production_year=production_year)

    def set_taxes(self):
        if self.production_year <= 2010:
            self.tax = 900
        else:
            self.tax = 200


# ==================================================================================================

def client_code(creator: CarCreator, production_year) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """
    new_car = creator.buy_car(production_year=production_year)
    print(f"Client just bought a new car", end="\n")
    print(f"Client has to pay {new_car.tax} in taxes", end="")


if __name__ == "__main__":
    print("Used BenzCreator class")
    client_code(BenzCreator(), 2000)
    print("\n")

    print("Used BmwCreator class")
    client_code(BmwCreator(), 2019)