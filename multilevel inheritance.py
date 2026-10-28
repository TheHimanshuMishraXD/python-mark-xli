class Animal:
    def __int__(self,name,species):
        self.name = name
        self.species = species

    def showdetails(self):
        print(f"name : {self.name}")
        print(f"species : {self.species}")


class Dog(Animal):
    def __int__(self,name,breed):
        Animal.__int__(self,name,species="Dog")
        self.breed = breed

    def showdetails(self):
        Animal.showdetails(self)
        print(f"breed : {self.breed}")



class Godenretirever:
    def __init__(self,name,colour):
        Dog.__int__(self,name,breed="Golden retriever")
        self.colour = colour


    def show_details(self):
        Dog.showdetails(self)
        print(f'colour: {self.colour}')

o = Godenretirever("tommy","black")
o.show_details()
print(Godenretirever.mro())

