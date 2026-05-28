print(" Welcome to ATM")

class ATM:
    def __init__(self,balance,pin):
        self.balance = balance
        self.pin = pin

    def check_pin(self):
        p = int(input("Enter PIN: "))
        if p == self.pin:
            return True
        else:
            print(f" Incorrect PIN!")
            return False

    def check_balance(self):
        print(f" Your balance is: ₹{self.balance}")


    def deposit(self):
        amt = int(input("Enter amount to deposit: ₹"))
        self.balance += amt
        print(f" ₹{amt} deposited successfully!")
        print(f" Updated balance: ₹{self.balance}")

    def withdraw(self):
        amt = int(input("Enter amount to withdraw: ₹"))
        if amt <= self.balance:
            self.balance -= amt
            print(f"Please collect your cash: ₹{amt}")
            print(f"Remaining balance: ₹{self.balance}")
        else:
            print(f"Insufficient balance! Available: ₹{self.balance}")

atm = ATM(10000,2345)


print(f"\n1. Check Balance")
print(f"2. Deposit")
print(f"3. Withdraw")
print(f"4. Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    if atm.check_pin():
        atm.check_balance()

elif choice == 2:
    if atm.check_pin():
        atm.deposit()

elif choice == 3:
    if atm.check_pin():
        atm.withdraw()

elif choice == 4:
    print(f"Thank you for using ATM!")

else:
    print(f" Invalid choice!")