import time
from os import system

    


    # agar kuch bulwana ho to
class Employee:
    emp_company = "MICROSOFT"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def showdetails(self):
        for name in {self.name}:
            system(f'say {self.name} is presented in the class')
        time.sleep(3)
        print(f"and this is my current salary : {self.salary}")
        time.sleep(2)
        print(f"this is my company where im currently working {self.emp_company}")

    
# e1 = Employee("MR HIMANSHU MISHRA",200000)
# e2 = Employee("Harsh Tiwari",100000)
calls = ()
for call in calls:
       print(system(f'Here first you need to enter your name first'))
e1 = Employee(input("enter ypur name:\n"),input("enter your salary:\n"))

e1.showdetails()
# e2.showdetails()


# import time

# class Student:
#     college = "SISTEC"

#     def __init__(self, name, roll_no, branch):
#         self.name = name
#         self.roll_no = roll_no
#         self.branch = branch

#     def showdetails(self):
#         print(f"So I am {self.name}")
#         time.sleep(2)
#         print(f"My roll number is: {self.roll_no}")
#         time.sleep(2)
#         print(f"My branch is: {self.branch}")
#         time.sleep(2)
#         print(f"My college is: {self.college}")


# s1 = Student("Himanshu Mishra", 101, "AI-DS")
# s2 = Student("Harsh Tiwari", 102, "CSE")

# s1.showdetails()
# # s2.showdetails()





