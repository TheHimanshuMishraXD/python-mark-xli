# Inheritance ka matlab hai ek class ka doosri class ke properties aur methods ko inherit (use) karna.

class  Employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
            print(f"the name of the eployee is {self.name} and id is {self.id}")
#from here we use the inheritance concept to create a new class which will inherit the properties of the employee class
class programmer(Employee):
     def showlanguage(self):
          print("python is a greate language")


# class Himanshu(programmer):
#      def showacc(self):
#           print("kya hai mere bhai sab badhiya hai ya nahi")


# class Person:
#      def __init__(self,name,age)
#      self.name = name
#      self,age = age

#      def showdetails(self):
#           print(f"hello everyone my name is {self.name}")


# class student(Person):
#      def __init__(self,name,age,)





e = Employee("Himanshu" , 200)
e.showDetails()
e = programmer("tINA" , 4000)
e.showDetails()
# e.showlanguage()
# e = Himanshu("Ram" , 474)
# e.showacc()



# 🟢 Practice Question: Company Employee
# Task

# Ek Employee class banao jisme:

# __init__() mein name aur salary lo.
# Ek method showDetails() banao jo name aur salary print kare.

# Phir ek Developer class banao jo Employee se inherit kare.

# Developer mein ek method showLanguage() banao jo print kare:
# Developer uses Python

# Phir ek SeniorDeveloper class banao jo Developer se inherit kare.

# SeniorDeveloper mein ek method showExperience() banao jo print kare:


# class Employee:
#      def __init__ (self,name,salary):
#           self._name = name
#           self._salary = salary

#      def showdetails(self):
#       print(f"Here is the employee name is {self._name} and the salary of the employee is {self._salary}")



# class devloper(Employee):
#           def showLanguage(self):
#                print("Devloper uses python")

# class seniordevloper(devloper):

#           def showexperience (self):
#                print("the devloper has 2 year of experience")


# s1 = seniordevloper("Himanshu" , 40)

# s1.showdetails()
# s1.showLanguage()
# s1.showexperience()


# #code dn

# #congo


# #show this is the question of inheritance







# #imp concept

       

















          
     
