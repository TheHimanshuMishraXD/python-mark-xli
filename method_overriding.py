# Method overriding is a feature in Python in which a child class defines a method with the same name as a method in its parent class,
#  providing its own implementation.
class shape:
    def __init__(self , x ,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)


    def area(self):
        return 3.14 * super().area()



# rec = shape(3,5)
# print(rec.area())


c = Circle(5)
print(c.area())


print("**************************this is the code by harry video*****************************************")