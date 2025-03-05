from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class NoDiscount(Discount):
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

# Використання
discount = PercentageDiscount(10)
print(discount.apply(100))
