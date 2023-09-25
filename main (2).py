class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance_inr = initial_balance

    def deposit(self, amount_inr):
        if amount_inr > 0:
            self.__account_balance_inr += amount_inr
            return f"Deposited ₹{amount_inr}. New balance: ₹{self.__account_balance_inr}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount_inr):
        if 0 < amount_inr <= self.__account_balance_inr:
            self.__account_balance_inr -= amount_inr
            return f"Withdrew ₹{amount_inr}. New balance: ₹{self.__account_balance_inr}"
        elif amount_inr > self.__account_balance_inr:
            return f"Insufficient funds. available balance ₹{self.__account_balance_inr}."
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Acc num:{self.__account_number}): ₹{self.__account_balance_inr}"

# Creating an instance of BankAccount
account = BankAccount("123456", "Jhon", 1000)

# Testing deposit and withdrawal functionality
print(account.display_balance())      # Display initial balance
print(account.deposit(500))            # Deposit ₹500
print(account.withdraw(400))          # Withdraw ₹400
print(account.withdraw(2000))          #withdraw more than balance
print(account.display_balance())
   #display updated balance
