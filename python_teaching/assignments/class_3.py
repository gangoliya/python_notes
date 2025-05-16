# Write a class called BankAccount with attributes account_holder and balance. 
# Include methods to deposit(amount) and withdraw(amount), and a method to display_balance(). 
# Implement the class with sample data.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def display_balance(self):
        print(f"The account balance for {self.account_holder} is {self.balance}.")

b1 = BankAccount("Rajesh", 10000)
b1.deposit(2000)
b1.withdraw(5000)
b1.display_balance()