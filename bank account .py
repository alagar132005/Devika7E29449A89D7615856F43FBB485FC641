class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"

# Example usage:
account = BankAccount("12345", "John Doe", 1000)
print(account.display_balance())  # Display initial balance

print(account.deposit(500))       # Deposit $500
print(account.withdraw(200))      # Withdraw $200
print(account.display_balance())  # Display updated balance
