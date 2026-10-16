# Definition: Python mein dir() ek built-in function hai jo kisi object ke available attributes aur methods ki list return karta hai.
# x = [1,2,3]
# print(dir(x))
# print(x.__add__)


# x = (1,2,3)
# print(dir(x))
# print(x.__add__)




# dict method in python
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



p = person("john" , 30)
print(p.__dict__)
        