# A Generator in Python is a special type of function that returns values one at a time using 
# the yield keyword instead of returning all values at once using return.

def my_generator():
    for i in range(500):
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:          
    print(j)

# yield – Value generate karta hai aur function pause karta hai.



# next() – Generator se next value leta hai.



# Generator – Large data ko efficiently process karne mein help karta hai.






# Python Generator – Coding Tasks
# Task 1 – Number Generator
# Easy

# Ek generator function my_generator() banao jo 1 se 10 tak numbers yield kare.

# Expected output:
# 1
# 2
# 3
# ...
# 10
   
  
# Condition: return ya list use nahi karna. yield use karna hai.

# Task 2 – Even Number Generator
# Easy

# Ek generator banao jo 1 se 20 tak sirf even numbers generate kare.

# Expected output:
# 2 4 6 8 10 12 14 16 18 20



# Task 3 – Next Function
# Medium

# Ek generator banao jo 5, 10, 15, 20 generate kare.

# next() ka use karke har value separately print karo.

# Task 4 – Custom Countdown
# Medium

# Ek generator banao jo 10 se 1 tak countdown kare.

# Task 5 – File Reader
# Real-world

# Ek generator function banao jo kisi text file ko line by line read kare aur yield kare.

# Let's start: Task 1
# Apna code yahan likh:

# Check my codeShow hint

# Pehle Task 1 complete kar. Main code review karke bataunga ki logic sahi hai ya nahi. 😎