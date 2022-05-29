from abc import ABC


class Drink(ABC):
    def __init__(self, name: str, origin: str, price: int):
        self.name = name
        self.origin = origin
        self.price = price


class Coffe(Drink):

    def __init__(self, name: str, origin: str, price: int, express: bool):
        self.express = express
        super().__init__(name, origin, price)


class Cacao(Drink):

    def __init__(self, name: str, origin: str, price: int):
        super().__init__(name, origin, price)


class Juice(Drink):

    def __init__(self, name: str, origin: str, price: int):
        super().__init__(name, origin, price)


class CofeeShop:

    def __init__(self, name: str, location: str, drink: Drink):
        self.name = name
        self.location = location
        self.drink = drink

    def pay(self):
        print(f"Pay {self.drink.price}$ for {self.drink.__class__.__name__.lower()}.")


if __name__ == '__main__':
    coffe = Coffe(name='Black Coffe', origin='Brazil', price=50, express=True)
    cacao = Cacao(name='Cacao', origin='Brazil', price=100)
    juice = Juice(name='Orange Juice', origin='Brazil', price=500)

    coffe_shop = CofeeShop(name='Alex Coffe Shop', location='Tirana', drink=coffe)
    coffe_shop.pay()