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


class PaymentProcessorSMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code: str):
        self.security_code = security_code

    def pay(self, order: Order):
        print("Processing Credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status('paid')


class DebitPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, security_code: str):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing Debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status('paid')


class PaypalPaymentProcessor(PaymentProcessorSMS):

    def __init__(self, email_address: str):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order: Order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.set_status('paid')


if __name__ == '__main__':
    order_1 = Order()
    order_1.add_item("Keyboard", 1, 50)
    order_1.add_item("SSD", 1, 150)
    order_1.add_item("USB cable", 2, 5)
    print(order_1.total_price())

    processor = CreditPaymentProcessor("2349875")
    processor.pay(order_1)
