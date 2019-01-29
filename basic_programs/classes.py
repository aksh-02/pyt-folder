class students:
 def __init__(self,nam,cl,marks):
  self.name=nam # nam is the argument passed and name is a characteristic of the object 
  self.cl=cl
  self.marks=marks
  
 def fn(self):
  self.name= self.name +' sharma' 

class boys(students): #class boys is inherited from class students
 pass
std1=students('ram',10,85)
print(std1.name)
std1.fn()
print(std1.name)
print(std1.__dict__)
abi=boys('abi',12,99)
print(abi.name)
abi.fn()
print(abi.marks)
print(abi.name)
