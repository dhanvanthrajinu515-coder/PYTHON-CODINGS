import datetime as dt

class juice:

    def __init__(self):
        self.orders=[]


    def orange_juice(self):
        a=int(input("quantity of orange juice: "))
        item = [100, a, "orange juice"]
        self.orders.append(item)
        x=open("orders.txt","a")
        x.write(f"order= orange juice = 100\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def apple_juice(self):
        b= int(input("quantity of apple juice: "))
        item1 = [100, b, "apple juice"]
        self.orders.append(item1)
        x=open("orders.txt","a")
        x.write(f"apple juice = 100\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def grapse_juice(self):
        c=int(input("quantity of grapse juice: "))
        item2 = [80, c, "grapse juice"]
        self.orders.append(item2)
        x=open("orders.txt","a")
        x.write(f"grapse juice = 80\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def watermelon_juice(self):
        d=int(input("quantity of watermelon juice: "))
        item3 = [50, d, "watermelon juice"]
        self.orders.append(item3)
        x=open("orders.txt","a")
        x.write(f"watermelon juice = 50\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def lemon_juice(self):
        e=int(input("quantity of lemon juice: "))
        item4 = [50, e, "lemon juice"]
        self.orders.append(item4)
        x=open("orders.txt","a")
        x.write(f"lemon juice = 50\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def rose_milk(self):
        f=int(input("quantity of rose milk: "))
        item5 = [60, f, "rose milk"]
        self.orders.append(item5)
        x=open("orders.txt","a")
        x.write(f"rose milk = 60\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def badam_milk(self):
        g=int(input("quantity of badam milk: "))
        item6 = [60, g, "badam milk"]
        self.orders.append(item6)
        x=open("orders.txt","a")
        x.write(f"badam milk = 60\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def vanilla_icecream(self):
        h=int(input("quantity of vanilla icecream: "))
        item7 = [100, h, "vanilla icecream"]
        self.orders.append(item7)
        x=open("orders.txt","a")
        x.write(f"vanilla icecream = 100\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def chocolate_icecream(self):
        i=int(input("quantity of chocolate icecream: "))
        item8 = [100, i, "chocolate icecream"]
        self.orders.append(item8)
        x=open("orders.txt","a")
        x.write(f"chocolate icecream = 100\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def strawberry_icecream(self):
        j=int(input("quantity of strawberry icecream: "))
        item9 = [150, j, "strawberry icecream"]
        self.orders.append(item9)
        x=open("orders.txt","a")
        x.write(f"strawberry icecream = 150\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def chocobar(self):
        k=int(input("quantity of chocobar: "))
        item10 = [70, k, "chocobar"]
        self.orders.append(item10)
        x=open("orders.txt","a")
        x.write(f"order=chocobar = 70\n")
        x.close()
        x=open("orders.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()

    def order_history(self):
        try:
            x=open("orders.txt","r")
            list=x.read()
            if list == "":
                print("no files")
            else:
                print(list)
            x.close()
        except FileNotFoundError:
            print("no files")


    def view_bill(self):
        if len(self.orders) == 0:
            print("Your bill is empty.")
            return

        print("\n--- CURRENT BILL ---")
        grand_total = 0
        for item in self.orders:
            price = item[0]
            quantity = item[1]
            name = item[2]
            item_total = price * quantity
            grand_total = grand_total + item_total
            print(f"{name}: {price} x {quantity} = {item_total}")

        print(f"Total Amount to Pay: {grand_total}\n")
        print("--- PAY THE BILL ---\n\n")



obj=juice()


while True:
    print("1.orange juice = 100")
    print("2.apple juice = 100")
    print("3.grapse juice = 80")
    print("4.watermelon juice = 50")
    print("5.lemon juice = 50")
    print("6.rose_milk = 60")
    print("7.badam milk = 60")
    print("8.vanilla_icecream = 100")
    print("9.strawberry_icecream = 150")
    print("10.chocobar = 70")
    print("11.order_history")
    print("12.view_bill")
    print("13.exit")


    choice=int(input("enter the food choice: "))

    if choice==1:
        obj.orange_juice()

    elif choice==2:
        obj.apple_juice()

    elif choice==3:
        obj.grapse_juice()

    elif choice==4:
        obj.watermelon_juice()

    elif choice==5:
        obj.lemon_juice()

    elif choice==6:
        obj.rose_milk()

    elif choice==7:
        obj.badam_milk()

    elif choice==8:
        obj.vanilla_icecream()

    elif choice==9:
        obj.strawberry_icecream()

    elif choice==10:
        obj.chocobar()

    elif choice==11:
        obj.order_history()

    elif choice==12:
        obj.view_bill()

    elif choice==13:
        print("Goodbye!")
        break

    else:
        print("enter the correct choice")

