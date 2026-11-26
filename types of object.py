class Employee:
    emp_comapny = "MICROSOFT"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        print(f"so I am {self.name}")
        print(f"and this is my current salary : {self.salary}")

    