from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of rs.{amount}")

class UPIpayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of rs.{amount}")

credit_card = CreditCardPayment()
upi = UPIpayment()

credit_card.process_payment(2000)
upi.process_payment(300)