
class RobotTesting:

    def __init__(self,employeeName , age , title , phone):
        self.employeeName = employeeName
        self.age = age
        self.title = title
        self.phone = phone


    address = "INDIA , CHENNAI"

    def addTwoNumbers(self,a,b):
        return a+b


#obj =  RobotTesting() 

#print(obj.address)
#print(obj.addTwoNumbers(3,2))

obj1 = RobotTesting("MITHUN" , 30  , "Senior QA Analyst" , "0123456789")

print(obj1.phone)