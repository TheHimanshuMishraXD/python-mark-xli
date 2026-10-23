# class vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i+{self.j}j+{self.k}k"

#     def __add__(self, x):
#         return f"{self.i + x.i}i+{self.j+x.j}j+{self.k+x.k}k"

# v1 = vector(4,5,6)
# print(v1)

# v2 = vector(6,7,8)
# print(v2)

# print(v1+v2)                  


# here the code is totally completed                

# 3 real-world examples
# 1. AI / Machine Learning 🤖

# Vectors aur matrices add karne mein:
# vector1 + vector2



# AI models mein numerical calculations hoti hain. Libraries jaise NumPy arrays ke saath + use karne deti hain.

# 2. E-commerce application 🛒

# Do shopping carts ke items combine karne ke liye:
# cart1 + cart2



# Is behaviour ko custom class mein __add__() se define kar sakte hain.

# 3. Banking system 💰

# Do custom money objects ko add karne ke liye:



# tasks----> Python OOP — Today's Practice Tasks 💻

# Task 1 — Vector Subtraction
# Easy
# Apni vector class mein __sub__() method bana, taaki do vectors ko - se subtract kar sake.

# Example:
# v1 = vector(10, 8, 6)v2 = vector(3, 2, 1)print(v1 - v2)



# Expected output: 7i+6j+5k



class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k


    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    def __sub__(self,x):
        return f"{self.i-self.x.i}i+{self.j-self.x.j}+{self.k-self.x.k}"

v1 = vector(4,5,6)
print(v1)

v2 = vector(7,8,9)
print(v2)



print(v1 - v2)