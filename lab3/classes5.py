class Account:
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Депозит: {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие: {amount}. Новый баланс: {self.balance}")


acc = Account("Асем", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)  