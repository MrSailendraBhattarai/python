# wap to calculate area of rectangle,square,circle from Area class.
import math
class Area:
    def __init__(self,length,width,radius):
        self.length=length
        self.width=width
        self.radius=radius
        # self.c =option

    
    def area(self):
        self.c=int(input("Enter Any Option \n 1: Rectangle \n 2: Square \n 3: Circle \n"))
        if self.c==1:
            self.c ="Rectangle"
            return self.rect()
        elif self.c==2:
            self.c = "Square"
            return self.squ()
        elif self.c==3:
            self.c = "Circle"
            return self.cir()

    def rect(self):
        return self.length*self.width
        

    def squ(self):
        return self.length**2
        

    def cir(self):
        return math.pi*self.radius**2
        # print(f"Area of Circle is: {area}")

    


A=Area(4,2,5)
result=A.area()
print(f"The area of {A.c} ",result)
A.rect()
A.squ()
A.cir()