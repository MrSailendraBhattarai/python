
class Calculator:
    sentence='of two number is: '
    def sum(self,a,b):
        print('Sum '+self.sentence,a+b)

    def sub(self,a,b):
        print('Subtract '+self.sentence,a-b)

    def mul(self,a,b):
        print('Multiply '+self.sentence,a*b)

    def div(self,a,b):
        print('Divide '+self.sentence,a/b)

c1=Calculator()
a=int(input("Enter number:  "))
b=int(input("Enter number:  "))
c1.sum(a,b)
c1.sub(a,b)
c1.mul(a,b)
c1.div(a,b)
