# defination of superkeyword in python -------- The super() function is used to call methods of a parent class from a child class without explicitly referring to the parent class.
#Hinglish mein: super() ka use child class ke andar parent class ke methods ya constructor (__init__) ko call karne ke liye hota hai.

class Parentclass:
    def parent_method(self):
        print("this is the parent method")


class childclass(Parentclass):
    def parent_method(self):
        print("himanshu")
    def child_method(self):
        print("this is the child method.")
        super().parent_method()


child_object = childclass()
child_object.child_method()
