# class Animal:
#     def __int__(self,name,species):
#         self.name = name
#         self.species = species

#     def showdetails(self):
#         print(f"name : {self.name}")
#         print(f"species : {self.species}")


# class Dog(Animal):
#     def __int__(self,name,breed):
#         Animal.__int__(self,name,species="Dog")
#         self.breed = breed

#     def showdetails(self):
#         Animal.showdetails(self)
#         print(f"breed : {self.breed}")



# class Godenretirever:
#     def __init__(self,name,colour):
#         Dog.__int__(self,name,breed="Golden retriever")
#         self.colour = colour


#     def show_details(self):
#         Dog.showdetails(self)
#         print(f'colour: {self.colour}')

# o = Godenretirever("tommy","black")
# o.show_details()
# print(Godenretirever.mro())

# 🐾 Task 1: Animal Inheritance System
# Easy · 15–20 min
# Goal: Animal → Cat → PersianCat

# Step 1: Animal class bana.
# - Constructor mein name aur species set kar.
# - show_details() method bana jo dono print kare.
# Step 2: Cat class bana jo Animal ko inherit kare.
# - Constructor mein name aur color le.
# - Parent constructor ko call karke species = "Cat" set kar.
# - show_details() override kar aur parent ki details bhi print kar.
# Step 3: PersianCat class bana jo Cat ko inherit kare.
# - Constructor mein name aur color le.
# - breed = "Persian" set kar.
# - Parent methods ka use karke saari details print kar.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showdetails(self):
        print(f"the name is : {self.name} and the species is {self.species}")


class cat(Animal):
    def __init__(self, name, color):
        self.color = color
        Animal.__init__(self,name,species="cat")

    def showdetails(self):
        Animal.showdetails(self)
        print(f"species: {self.color}")

class persiancat(cat):
    def __init__(self, name, color):
        super().__init__(name,color)
        self.breed = "persian"

o = persiancat("billa", "rampuri")
o.showdetails()
        
        