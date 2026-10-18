# defination of superkeyword in python -------- The super() function is used to call methods of a parent class from a child class without explicitly referring to the parent class.
#Hinglish mein: super() ka use child class ke andar parent c
# lass ke methods ya constructor (__init__) ko call karne ke liye hota hai.

# class Parentclass:
#     def parent_method(self):
#         print("this is the parent method")


# class childclass(Parentclass):
#     # def parent_method(self):
#     #     print("himanshu")
#     #     super().parent_method()
#     def child_method(self):
#         print("this is the child method.")
#         super().parent_method()


# child_object = childclass()
# child_object.child_method()
# child_object.parent_method(

# # )            

# class Employee:
#     def __init__(self, name , id ):
#         self.name = name
#         self.id= id


# class programmer(Employee):
#     def __init__(self,name,id,lang):
#         super().__init__(name,id)
#         self.lang = lang

# rohan = Employee("rohan","242")
# himanshu = programmer("himanshu" , "8383" , "python")
# print(himanshu.name)
# print(himanshu.id)
# print(himanshu.lang)




# Level 1: Student Management 🎯
# Task: Ek Person class banao aur usse Student class inherit karao.
# Expected output:
# Name: Himanshu
# Age: 19
# Course: AI & DS


# Hints:
# 1. Person class mein __init__(self, name, age) banao.
# 2. Student class ko Person se inherit karao.
# 3. Student ke constructor mein name, age aur course parameters lo.
# 4. super() ki help se parent class ka constructor call karo.
# 5. course ko child class ke object mein store karo.
# Concept: super().__init__(name, age)



class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class student(person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course


child_class = person("himanshu","19")
print(child_class.name)
print(child_class.age)

child_class1 = student("himanshu","19")
child_class1.name
child_class1.age