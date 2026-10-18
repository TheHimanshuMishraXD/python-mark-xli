# 1. Magic Methods in Python
# Definition (English): Magic methods are special methods in Python that allow objects to interact with built-in operations such as addition, comparison, and string representation.
# Hinglish: Magic methods Python ke special methods hote hain, 
# jo objects ke saath built-in operations ko define karne mein help karte hain.


# # class Employee:
# #     name = "himanshu"


# # e = Employee()
# # print(e.name)
# # print(len(e)) ----> ┌──(batman㉿mark-xli)-[~/python code with harry]
# # └─$ /usr/bin/python "/home/batman/python code with harry/magic and dunder method.py"
# # himanshu
# # Traceback (most recent call last):
# #   File "/home/batman/python code with harry/magic and dunder method.py", line 7, in <module>
# #     print(len(e))
# #           ~~~^^^
# # TypeError: object of type 'Employee' has no len()
# Hinglish mein: __repr__() ek special method hai jo object ka detailed aur unambiguous string representation return karta hai,
# jisse developers object ko easily samajh aur debug kar sakein.


from emp import Employee
# class Employee:
#     name = "Harry"
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i + 1
#         return i


e = Employee("Himanshu")
print(str(e))
print(repr(e))
e()                          