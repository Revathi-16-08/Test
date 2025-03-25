# acquiring properties from parent to child

from OOPS import calculator

class child_import(calculator):
    num2 =200

    def __init__(self):
        calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num +self.summation()
        

obj =child_import()
print(obj.getCompleteData())