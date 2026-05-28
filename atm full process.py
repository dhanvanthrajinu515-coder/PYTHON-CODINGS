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

        x =open("transaction history.txt", "a")
        x.write(f"deposit: {amt}\n")
        x.close()
        x=open("transaction history.txt","w")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def withdraw(self):
        amt = int(input("Enter amount to withdraw: ₹"))
        if amt <= self.balance:
            self.balance -= amt
            print(f"Please collect your cash: ₹{amt}")
            print(f"Remaining balance: ₹{self.balance}")

            x=open("transaction history.txt", "a")
            x.write(f"withdraw: {amt}\n")
            x.close()
            x=open("transaction history.txt", "w")
            x.write(f"{dt.datetime.now()}\n\n")
            x.close()

    def transaction_history(self):
       x=open("transaction history.txt","r")
       data=x.read()

       if data == "":
           print("Transaction history is empty!")
       else:
           print(data)

       x.close()


atm = ATM(10000,2345)

while True:
    print(f"\n1. Check Balance")
    print(f"2. Deposit")
    print(f"3. Withdraw")
    print(f"4. transaction_history")
    print(f"5. exit")

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
      if atm.check_pin():
          atm.transaction_history()


    elif choice == 5:
        print(f"Thank you for using ATM!")


    else:
        print(f" Invalid choice!")
