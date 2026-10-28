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

