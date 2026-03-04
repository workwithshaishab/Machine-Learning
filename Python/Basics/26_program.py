"""
Define a class BankAccount with:

Attributes: account_number, account_holder, and balance.

Methods:

deposit(amount) → adds amount to balance

withdraw(amount) → subtracts amount from balance if enough balance exists

display() → prints account details

Create two accounts and perform some deposits and withdrawals.

Print the final details of both accounts.
"""

class BankAccount:
    def __init__(self, ac_num, ac_holder, balance):
        self.ac_num= ac_num
        self.ac_holder=ac_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Insufficient balance!!")
        self.balance-=amount

    def display(self):
        print("Account Details:", self.ac_num, "\nAccount Holder:", self.ac_holder, "\nAccount Balance:", self.balance)

bank1= BankAccount(1, "Fermin Lopez", 0)
bank2= BankAccount(2, "Pedri Gonzalez", 0)

bank1.deposit(1200)
bank2.deposit(1000)

bank1.withdraw(800)
bank2.withdraw(200)

bank1.display()
bank2.display()