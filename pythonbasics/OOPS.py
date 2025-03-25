#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be _init_
#new keyword is not required when you create obj like in java

class calculator:
    num =100 # class variables
#functions and methods are same.
    #default constructor

    def __init__(self, a, b):
        self.firstnumber =a
        self.secondnumber =b
        print("I am called automatically when obj is created")

    def getdata(self):
        print("I am now executing as method in class")
    def summation(self):
        return self.firstnumber + self.secondnumber + calculator.num

obj= calculator(2, 3) #create objects in python
obj.getdata()
print(obj.summation())

obj= calculator(2, 5) #create objects in python
obj.getdata()
print(obj.summation())
