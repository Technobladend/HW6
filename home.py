class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, overdraft_limit, balance=0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def list_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Owner: {account.owner}, Balance: {account.balance}")

    def total_funds(self):
        total = sum(account.get_balance() for account in self.accounts)
        print(f"Total funds in the bank: {total}")
        return total


class SavingsAccount(BankAccount):

    def __init__(self, account_number, balance, owner, interest_rate ):
        super().__init__(account_number=account_number, balance=balance, owner=owner)
        self.interest_rate = interest_rate


    def add_interest(self):
        self.balance += (self.balance * self.interest_rate / 100)
        return self.balance

# Создаем счета
checking = CheckingAccount("CA54321", "Bob", 500, 200)

# Создаем банк и добавляем счета
bank = Bank("MyBank")
bank.add_account(checking)

# Действия с счетами

checking.withdraw(600)
checking.deposit(300)

# Выводим список счетов и общую сумму денег в банке
bank.list_accounts()
bank.total_funds()


save_acc = SavingsAccount("CFG234F", 100, "Umar", 10)
save_acc.withdraw(600)
save_acc.deposit(300)
