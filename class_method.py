# A class method is a method that takes the class itself as its first parameter, 
# represented by cls, and is defined using the @classmethod decorator.
# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"the name is {self.name} and the company name is {self.company}")

#     @classmethod
#     def changeCompany(cls,newcompany):
#         cls.company = newcompany



# e1 = Employee()
# e1.name = "Himanshu"
# e1.show()

# e1.changeCompany("Tesla")
# e1.show()                         
# print(Employee.company)          this is the code guys    ??wow guys



# 1. Employee Company Updater

# Employee class banao.

# Requirements:
# 1. Class variable company = "Apple" rakho.
# 2. @classmethod change_company(cls, new_company) banao.
# 3. Do employee objects create karo.
# 4. Company ko Tesla mein change karke dono objects ka company name print karo.


# class Employee:
#     company = "Apple"

#     def show(self):
#         print(f"hello my name is {self.name} and my company is {self.company}")


#     @classmethod
#     def change_company(cls,new_company):
#         cls.company = new_company




# a = Employee()
# a.name = "himanshu"
# a.show()
# a.change_company("Tesla")
# a.show()



# Bank Management System
# Ek BankAccount class bana, jisme:
# 1. Class variable bank_name = "SBI" ho.
# 2. __init__() mein account holder ka naam aur balance store ho.
# 3. @classmethod change_bank(cls, new_name) bank ka naam update kare.
# 4. Do objects banao — Himanshu aur Rahul.
# 5. Bank name ko "HDFC" mein change karo.
# 6. Dono accounts ka holder name, balance aur bank name print karo.
# Condition: Is baar __init__() ka use bhi karna hai. Hint: self.name = name aur self.balance = balance.

class bankAccount:
    bank_name = "Sbi"
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    @classmethod
    def change_bank(cls,newbank_name):
        cls.bank_name = newbank_name
        