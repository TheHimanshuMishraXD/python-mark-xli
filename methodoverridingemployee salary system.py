# 🧑‍💻 Task 1: Employee Salary System
# Employee Management System

# Difficulty: Easy–Medium
# Ek Python program bana jo normal employee aur manager ki salary calculate kare.
# Requirements:
# - Employee naam ki parent class banao.
# - Constructor mein name aur salary store karo.
# - show_details() method employee ki details print kare.
# - Manager naam ki child class banao jo Employee ko inherit kare.
# - Manager ke constructor mein name, salary aur bonus lo.
# - super() use karke parent constructor call karo.
# - show_details() ko Manager class mein override karo.
# - Manager ki total salary = basic salary + bonus.

# Expected output
# Tere program ka output kuch aisa aana chahiye:
# Employee Name: Rahul
# Salary: 25000

# Manager Name: Aman
# Basic Salary: 50000
# Bonus: 10000
# Total Salary: 60000


# VS Code mein kya karna hai?
# 1. employee.py naam ki file bana.
# 2. Upar diye gaye requirements ke according khud code likh.
# 3. Program run kar aur output check kar.
# 4. Apna code yahan paste kar de — main teacher ki tarah mistakes samjhaunga, seedha solution nahi dunga.
# Rule: Google ya mera solution copy nahi karna. Khud try karna, atke toh hint maang lena.

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def showdetails(self):
        print(f"so the employee name is {self.name} and the employee age is {self.age} and the salary of the employee is {self.salary}")


class Manager(Employee):
    def __init__(self,name,age,salary , bonus):
        self.salary = salary
        self.bonus = bonus
        self.age = age
        super().__init__(name,salary,age,bonus)

