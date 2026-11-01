# Walrus Operator (:=) in Python
# Definition: Walrus operator (:=) Python ka ek assignment operator hai, 
# jo kisi variable ko value assign karne ke saath-saath usi expression mein us variable ki value use karne ki facility deta hai.

# a = True
# print(a:= False)
# print(a)

# numbers = [10,20,30,40,50]

# while ( n:= len(numbers)) > 0:
#     print(numbers.pop())



# happy = False
# print(happy)


# print(happy := True)




# food = list()
# while True:
#     item = input("what do you like as a food   : ")
#     if item == "quit":
#         break
#     food.append(item)



# foods = list()
# while (foods > 5) (food := input("enter the food you likr")) != "quit":
#     foods.append(food)

# print(foods)

    # if len(food) > 5:
    #     break
    # print(f"you have enterd this kind of food {len(foods)} times")




# food = list()

# n = int(input("How many foods do you want to enter? "))

# i = 0

# while (item := input("Enter your food: ")) and i < n:
#     food.append(item)
#     i += 1

# print("Your foods are:", food)


# foods = list()

# n = int(input("enter how many food you want to enter:  "))

# i = 0

# while(item := input("what food you like mostly:  ")) and i < n:
#     foods.append(item)

#     i = i + 1

# print("your food are:" , foods)




foods = list()
n = int(input("how many food you wants to enter"))


for i in range(n):
    food = input("what is the food you like mostly:  ")
    foods.append(food)

print(f"this is your food you like mostly {foods}")
