x=open("vehicle details.txt","w")
x.write("parking details\n")
x.close()

import datetime as dt

print("parking vehicle details")

class vehicle_details():
    def details(self):
        detail1 =input("enter vehicle brand: ")
        detail2 =input("enter vehicle model: ")
        detail3 =input("enter vehicle register number : ")
        detail4 =input("enter vehicle colour: ")
        detail5 =input("enter vehicle type: ")  #Ex: 2 wheeler or 4 wheeler or 5 or 6
        detail6 =int(input("enter vehicle parking slot number: "))

        x=open("vehicle details.txt","a")
        x.write("\n---------START----------\n\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle brand: {detail1}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle model: {detail2}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle register number : {detail3}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle colour: {detail4}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle type: {detail5}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"vehicle parking slot number: {detail6}\n\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write(f"{dt.datetime.now()}\n\n")
        x.close()


        print("details added successfully")


    def parking_price(self):

        detail7=int(input("enter vehicle parking hours: ")) #Ex: 1 hour or 5 hours or 10 hours
        if(detail7<5):
          print("-----------------")
          print("price = 50 Rupees")
          print("-----------------")
        elif(detail7>=5 and detail7<10):
          print("------------------")
          print("price = 100 Rupees")
          print("------------------")

        elif(detail7>=10 and detail7<20):
          print("------------------")
          print("price = 150 Rupees")
          print("------------------")
        elif(detail7>=20 and detail7<30):
          print("------------------")
          print("price = 200 Rupees")
          print("------------------")
        elif(detail7>=30 and detail7<40):
          print("------------------")
          print("price = 250 Rupees")
          print("------------------")
        elif(detail7>=40 and detail7<50):
          print("------------------")
          print("price = 300 Rupees")
          print("------------------")
        else:
          print("enter the hours")

        x=open("vehicle details.txt","a")
        x.write(f"parking hours:{detail7}\n")
        x.close()

        x=open("vehicle details.txt","a")
        x.write("----------END---------\n\n")



    def view_history(self):
        try:
            x=open("vehicle details.txt","r")
            list=x.read()
            if list == "":
                print("no files")
            else:
                print(list)
            x.close()
        except FileNotFoundError:
            print("no files")

obj = vehicle_details()

while True:
    print("1.details")
    print("2.parking_price")
    print("3.view_history")


    choice=int(input("enter your choice: "))

    if choice == 1:
        obj.details()

    elif choice == 2:
        obj.parking_price()

    elif choice == 3:
        obj.view_history()
    else:
        print("enter the choice")
