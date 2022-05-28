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

    @abstractmethod
    def pay(self, order):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing Credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status('paid')


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing Debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status('paid')


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str):
        self.email_address = email_address

    def pay(self, order: Order):
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.set_status('paid')


if __name__ == '__main__':
    order_1 = Order()
    order_1.add_item("Keyboard", 1, 50)
    order_1.add_item("SSD", 1, 150)
    order_1.add_item("USB cable", 2, 5)

    print(order_1.total_price())

    debit_processor = DebitPaymentProcessor(security_code="0372846")
    debit_processor.pay(order=order_1)

    paypal_processor = PaypalPaymentProcessor(email_address="alex@gmail.com")
    paypal_processor.pay(order=order_1)
