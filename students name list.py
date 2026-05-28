class students:
    def __init__(self):
        self.names = []


    def add_students(self):
        num= int(input("number of students want to add? "))
        for i in range(num):
            name=input("enter the name")
            self.names.append(name)
        print("successfully added!")

    def remove_students(self):
        n= input("Enter student name: ")
        for n in self.names:
            index_no=self.names.index(n)
            self.names.pop(index_no)
            print("successfully removed!")

    def view_list_of_students(self):
        for s,(n) in enumerate(self.names,1):
            print(self.names)

    def asc_order(self):
        self.names.sort()
        print(self.names)


obj=students()

while True:
    print("1.add_students")
    print("2.remove_student")
    print("3.view_list_of_students")
    print("4.asc_order")
    print("5.exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
      obj.add_students()

    elif choice == 2:
      obj.remove_students()

    elif choice == 3:
      obj.view_list_of_students()


    elif choice == 4:
      obj.asc_order()

    elif choice == 5:
        print("thank you!")

else:
    print(f" Invalid choice!")

