class Employee:
    emp_company = "MICROSOFT"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        print(f"so I am {self.name}")
        print(f"and this is my current salary : {self.salary}")
        print(f"this is my company where im currently working {emp_comp}")

    
# e1 = Employee("MR HIMANSHU MISHRA",200000)
# e2 = Employee("Harsh Tiwari",100000)
e1 = Employee(input("enter ypur name:\n"),input("enter your salary:\n"))

e1.showdetails()
# e2.showdetails()