# OOPs(Object oriented programming and systems)
class Item:
    discount = 0.2

    def __init__(self, name: str, price: float = 0.0, quantity: int = 0):
        # Assertion
        assert price >= 0, "Price cannot be less then zero"
        assert quantity >= 0, "Qunatity cannot be less then 0 "

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price - (self.price * self.discount)


item1 = Item("Phone", 100, 50)
item2 = Item("Laptop", 30000, 10)

item1.apply_discount()
print("price of item1 is ===>>>> ", item1.price)

item2.discount = 0.1
item2.apply_discount()
print("Price of item 2 is ===>>> ", item2.price)