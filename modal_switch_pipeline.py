from abc import ABC, abstractmethod

# CONTRACT (Abstraction)
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price

class VIPDiscount(DiscountStrategy):
    def apply(self, price: float) -> float:
        return price * 0.8  # -20%

# CONTEXT (Folosește polimorfismul)
class Order:
    def __init__(self, price: float, discount: DiscountStrategy):
        self.price = price
        self._strategy = discount  # Corectat: folosim argumentul 'discount'

    def set_strategy(self, strategy: DiscountStrategy): # Redenumit pentru claritate
        print(f"--- SCHIMBARE STRATEGIE LA: {strategy.__class__.__name__} ---")
        self._strategy = strategy

    def get_total(self):
        # Polimorfism: nu știm ce discount e, dar știm că are metoda .apply() [2]
        return self._strategy.apply(self.price)

# EXECUȚIE
order = Order(100.0, NoDiscount())
print(f"Preț inițial: {order.get_total()}")

order.set_strategy(VIPDiscount()) # Apelare corectă a metodei
print(f"Cost final după upgrade: {order.get_total()}")
