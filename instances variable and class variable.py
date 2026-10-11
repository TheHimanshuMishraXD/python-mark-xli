class Employee:
    def __init__(self,name):
        self.name = name 
    def showdetails(self):
            print(f"this is the details of the employee name is {self.name}")


e = Employee("Himanshu")
e.showdetails()
Employee.showdetails()   # ye dono ik hi chiz return karege chahe kaisi bhi ho wo chiz