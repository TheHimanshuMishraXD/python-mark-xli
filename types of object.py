class Employee:
    emp_comapny = "MICROSOFT"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        print(f"so I am {self.name}")
        print(f"and this is my current salary : {self.salary}")

    
# e1 = Employee("MR HIMANSHU MISHRA",200000)
# e2 = Employee("Harsh Tiwari",100000)
e1 = Employee(input("enter ypur name"),input("enter your salary"))

e1.showdetails()
e2.showdetails()