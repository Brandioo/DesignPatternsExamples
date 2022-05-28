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


class PaymentProcessor:

    @staticmethod
    def pay_credit(order: Order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status('paid')

    @staticmethod
    def pay_debit(order: Order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_status('paid')


if __name__ == '__main__':
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())

    PaymentProcessor.pay_debit(order=order, security_code="0372846")
