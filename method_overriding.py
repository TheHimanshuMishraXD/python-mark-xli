# Method overriding is a feature in Python in which a child class defines a method with the same name as a method in its parent class,
#  providing its own implementation.
class shape:
    def __init__(self , x ,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class circle(shape):
    def __init__(self,radius):
        self.radius = radius


    # def area(self):
    #     return 3.14*self.radius*self.radius



# rec = shape(3,5)
# print(rec.area())


c = circle(5)
print(c.area())