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



foods = list()
while (food := input("enter the food you likr")) != "quit":
    foods.append(food)

    if len(food) > 5:
        break
    print(f"you have enterd this kind of food {len(foods)} times")
