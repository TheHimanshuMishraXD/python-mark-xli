class Employee:
    def __init__(self):
        def __init__ (self,name):
            self.name = name
    def showdetails(self):
                    print(f"my name is{self.name}")
        
    
        

class dancer:
    def __init__(self,dance):
         self.dance = dance
    def showdetails1(self):
                    print(f"my dance is{self.dance}")
        
    
    
class DancerEmployee(Employee,dancer):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

a = DancerEmployee("Himanshu","kathak")
print(a.name)
print(a.dance)
a.showdetails1()

# mro method -- method resolution order
print(DancerEmployee.mro())


