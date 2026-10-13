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
# print(Employee.company)          this is the code guys    ??wow guys



# 1. Employee Company Updater

# Employee class banao.

# Requirements:
# 1. Class variable company = "Apple" rakho.
# 2. @classmethod change_company(cls, new_company) banao.
# 3. Do employee objects create karo.
# 4. Company ko Tesla mein change karke dono objects ka company name print karo.


class Employee:
    company = "Apple"

    def show(self):
        print(f"hello my name is {self.name} and my company is {self.company}")


    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company




a = Employee()
a.company