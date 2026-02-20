class BankAccount:
    account_count = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        BankAccount.account_count += 1

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    @classmethod
    def get_account_count(cls):
        return cls.account_count

    @staticmethod
    def convert_to_eur(usd_amount, rate=0.91):
        return usd_amount * rate

a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 500)

a1.deposit(500)
a2.withdraw(200)

print(f"{a1.owner} balance: ${a1.get_balance()}")
print(f"{a2.owner} balance: ${a2.get_balance()}")
print(f"Total accounts created: {BankAccount.get_account_count()}")
print(f"${a1.get_balance()} in EUR: €{BankAccount.convert_to_eur(a1.get_balance()):.2f}")
