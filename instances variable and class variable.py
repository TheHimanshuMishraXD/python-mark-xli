# Definition: An instance variable is a variable that belongs to an object of a class and stores data specific to that  
# particular object.
#  It is usually defined using self inside a class.


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Instance Variable: Python mein instance variable woh variable hota hai jo class ke kisi particular object ka data store karta hai. 
# Isse usually self keyword ki help se define kiya jata hai, aur har object ki is variable mein alag value ho sakti hai
class Employee:
    companyName = "Microsoft"
    def __init__(self,name):
        self.name = name 
        self.raise_amount = 40000
    def showdetails(self):
            print(f"this is the details of the employee name is {self.name}  , and the raise amount is {self.raise_amount} and the company name is {self.companyName}")

# Employee.showdetails(e) 
e = Employee("Himanshu")
e.companyName = "SAFARI"
e.showdetails()
e1 = Employee("Harsh")
e1.showdetails()
e1.raise_amount = 456
e1.showdetails()
# Employee.showdetails(e)  #isme hamko ik argument paas karna hi hoga chahe jaise bhi 
# # ye dono ik hi chiz return karege chahe kaisi bhi ho wo chiz