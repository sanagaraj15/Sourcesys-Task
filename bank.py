class BankAccount:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_details(self):
        print("\n----- Account Details -----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")


# Creating Object
name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")

account1 = BankAccount(name, acc_no)

while True:
    print("\n----- Bank Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)

    elif choice == 3:
        account1.check_balance()

    elif choice == 4:
        account1.display_details()

    elif choice == 5:
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice! Try again.")
