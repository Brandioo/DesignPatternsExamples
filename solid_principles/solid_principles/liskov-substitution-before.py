from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def set_status(self, status):
        self.status = status


class PaymentProcessor(ABC):

    @staticmethod
    @abstractmethod
    def pay(order, security_code):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    @staticmethod
    def pay(order: Order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status('paid')


class DebitPaymentProcessor(PaymentProcessor):

    @staticmethod
    def pay(order: Order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status('paid')


class PaypalPaymentProcessor(PaymentProcessor):

    @staticmethod
    def pay(order: Order, security_code):
        print("Processing PayPal payment type")
        print(f"Verifying security code using email: {security_code}")
        order.set_status('paid')


if __name__ == '__main__':
    order_1 = Order()
    order_1.add_item("Keyboard", 1, 50)
    order_1.add_item("SSD", 1, 150)
    order_1.add_item("USB cable", 2, 5)

    print(order_1.total_price())

    PaypalPaymentProcessor.pay(order=order_1, security_code="0372846")
