# Definition: An instance variable is a variable that belongs to an object of a class and stores data specific to that  
# particular object.
#  It is usually defined using self inside a class.
class Employee:
    def __init__(self,name):
        self.name = name 
    def showdetails(self):
            print(f"this is the details of the employee name is {self.name}")


e = Employee("Himanshu")
e.showdetails()
Employee.showdetails(e)  #isme hamko ik argument paas karna hi hoga chahe jaise bhi # ye dono ik hi chiz return karege chahe kaisi bhi ho wo chiz