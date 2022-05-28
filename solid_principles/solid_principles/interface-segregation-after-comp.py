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


class SMSAuth:
    authorized = False

    def verify_code(self, code: str):
        print(f'Verifying code {code}')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


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

    def __init__(self, security_code: str, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing Debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_status('paid')


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address: str, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order: Order):
        if not self.authorizer.is_authorized():
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

    sms_auth = SMSAuth()
    sec_code = "2349875"
    processor = DebitPaymentProcessor(security_code=sec_code, authorizer=sms_auth)
    sms_auth.verify_code(code=sec_code)
    processor.pay(order_1)
