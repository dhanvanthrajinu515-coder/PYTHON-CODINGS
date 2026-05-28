class marks:
    def __init__(self):
        self.name = []
        self.marks = []

    def check_pin1(self):
        p = int(input("Enter PIN: "))
        if p == 1234:
            return True
        else:
            print(f" Incorrect PIN!")
            return False

    def check_pin2(self):
        p = int(input("Enter PIN: "))
        if p == 2345:
            return True
        else:
            print(f" Incorrect PIN!")
            return False


    def check_pin3(self):
        p = int(input("Enter PIN: "))
        if p == 3456:
            return True
        else:
            print(f" Incorrect PIN!")
            return False


    def check_pin4(self):
        p = int(input("Enter PIN: "))
        if p == 4567:
            return True
        else:
            print(f" Incorrect PIN!")
            return False

    def check_pin5(self):
        p = int(input("Enter PIN: "))
        if p == 5678:
            return True
        else:
            print(f" Incorrect PIN!")
            return False

    def vishva(self):
        print("------Result-------")
        print("vishva marks:\n")
        print("tamil = 65")
        print("English = 75")
        print("mathematics = 70")
        print("science = 83")
        print("social science = 80\n")
        print("====== total marks = 373 ========")

        x=open("history.txt","a")
        x.write(f"vishva viewed: {dt.datetime.now()}\n\n")
        x.close()

    def akhil(self):
        print("------Result-------")
        print("akhil marks:\n")
        print("tamil = 68")
        print("English = 65")
        print("mathematics = 90")
        print("science = 73")
        print("social science = 50\n")
        print("====== total marks = 346 ========")

        x=open("history.txt","a")
        x.write(f"akhil viewed: {dt.datetime.now()}\n\n")
        x.close()

    def surya(self):
        print("------Result-------")
        print("surya marks:\n")
        print("tamil = 67")
        print("English = 95")
        print("mathematics = 72")
        print("science = 78")
        print("social science = 61\n")
        print("====== total marks = 373 ========")

        x=open("history.txt","a")
        x.write(f"surya viewed: {dt.datetime.now()}\n\n")
        x.close()

    def dhanvanth(self):
        print("------Result-------")
        print("dhanvanth marks:\n")
        print("tamil = 64")
        print("English = 85")
        print("mathematics = 77")
        print("science = 93")
        print("social science = 75\n")
        print("====== total marks = 346 ======== ")

        x=open("history.txt","a")
        x.write(f"dhanvanth viewed: {dt.datetime.now()}\n\n")
        x.close()

    def hari(self):
        print("------Result-------")
        print("hari marks:\n")
        print("tamil = 68")
        print("English = 65")
        print("mathematics = 90")
        print("science = 73")
        print("social science = 50\n")
        print("====== total marks = 346 ========")


        x=open("history.txt","a")
        x.write(f"hari viewed: {dt.datetime.now()}\n\n")
        x.close()

obj = marks()

while True:
    print("1.vishva")
    print("2.akhil")
    print("3.surya")
    print("4.dhanvanth")
    print("5.hari")

    choice=(input("Enter your choice: "))

    if choice=="1":
        if obj.check_pin1():
            obj.vishva()

    elif choice=="2":
       if  obj.check_pin2():
            obj.akhil()

    elif choice=="3":
        if obj.check_pin3():
            obj.surya()

    elif choice=="4":
        if obj.check_pin4():
            obj.dhanvanth()

    elif choice=="5":
        if obj.check_pin5():
            obj.hari()

    else:
        print("invalid input")