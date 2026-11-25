"""Factory worked example: create payment methods by name."""


class CreditCard:
    def __init__(self, number):
        self.number = number

    def pay(self, amount):
        return f"Charged {amount:.2f} to card ending {self.number[-4:]}"


class PayPal:
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Charged {amount:.2f} to PayPal account {self.email}"


class BankTransfer:
    def __init__(self, iban):
        self.iban = iban

    def pay(self, amount):
        return f"Requested transfer of {amount:.2f} from {self.iban}"


PAYMENT_METHODS = {
    "card": CreditCard,
    "paypal": PayPal,
    "bank": BankTransfer,
}


def create_payment_method(kind, *args, **kwargs):
    """The factory: callers never import or name the concrete classes."""
    try:
        cls = PAYMENT_METHODS[kind]
    except KeyError:
        raise ValueError(f"Unknown payment method: {kind}") from None
    return cls(*args, **kwargs)


if __name__ == "__main__":
    checkout = [
        ("card", ("4111111111111111",)),
        ("paypal", ("ana@example.com",)),
        ("bank", ("DE89370400440532013000",)),
    ]
    for kind, args in checkout:
        print(create_payment_method(kind, *args).pay(49.9))
    try:
        create_payment_method("crypto")
    except ValueError as err:
        print("Error:", err)
