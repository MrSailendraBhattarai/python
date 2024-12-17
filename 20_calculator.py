
n1=float(input("Enter Number: "))
n2=float(input("Enter Number: "))

n=int(input(print("Enter Any Options:\n 1:- Add \n 2:- Subtract \n 3:- Multiply \n 4:- Divide \n ")))

def sum():
    n3=n1+n2
    print("Sum= ",n3)
def sub():
    n3=n1-n2
    print("Subtract= ",n3)
def mul(): 
    n3=n1*n2
    print("Multiply= ",n3)
def div():
    n3=n1/n2
    print("Divide= ",n3)

if n==1:
    sum()
elif n==2:
    sub()
elif n==3:
    mul()
elif n==4:
    div()
else:
    print("Give valid Input: ")