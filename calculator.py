import json

class calculate:
 
 def __init__(self):
    self.first = int(input("Enter the first value: "))
    self.second = int(input("Enter the second value: "))


 def add(self):
    return self.first+self.second
  
 def substract(self):
    return self.first-self.second
  
 def multiply(self):
    return self.first*self.second
  
 def divide(self):
    return self.first/self.second

print("Enter the choice")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")

choice=input("Enter the choice")

calc=calculate()

if choice=="1":
  print("ans",calc.add())

if choice=="2":
   print("ans",calc.substract())

if choice=="3":
   print("ans",calc.multiply())

if choice=="4":
   print("ans",calc.divide())

