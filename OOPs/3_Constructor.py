class Calculator:
    def __init__(self,a,operator,b):
        self.a=a
        self.b=b
        self.operator=operator
    
    def result(self):
        if self.operator=='+':
            return self.add()
        elif self.operator=='-':
            return self.sub()
        elif self.operator=='*':
            return self.mul()
        else:
            return self.div()

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b


a=int(input("Enter number:  "))
b=input("Enter Operator: ")
c=int(input("Enter number:  "))

cal_obj=Calculator(a,b,c)
output=cal_obj.result()
print("Calculation =  ",output)