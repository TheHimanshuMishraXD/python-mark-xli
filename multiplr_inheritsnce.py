class Employee:
    def __init__(self):
        def __init__ (self,name):
            self.name = name


class dancer:
    def __init__(self,dance):
         self.dance = dance

class DancerEmployee(Employee,dancer):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

a = DancerEmployee("Himanshu,kathak")
print(a)