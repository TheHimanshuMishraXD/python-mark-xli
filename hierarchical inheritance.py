class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name}")


class Dog(Animal):
    def bark(self):
        print("Dog barks!")


class Cat(Animal):
    def meow(self):
        print("Cat meows!")


d = Dog("Tommy")
d.show()
d.bark()

c = Cat("Kitty")
c.show()
c.meow()