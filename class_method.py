# A class method is a method that takes the class itself as its first parameter, 
# represented by cls, and is defined using the @classmethod decorator.
class Employee:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and the company name is {self.company}")

    @classmethod
    def changeCompany(cls,newcompany):
        cls.company = newcompany



e1 = Employee()
e1.name = "Himanshu"
e1.show()

e1.changeCompany("Tesla")
e1.show()
print(Employee.company)