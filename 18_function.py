# def add():
#     a = 5
#     b = 4
#     print(a+b)

# wap to make simple calculator using function
a=int(input("Enter First number: "))
operator=input("Enter operator: ")
b=int(input("Enter Second number:"))

# always make function first otherwise it will show error
def sum():
    sum=a+b
    print("Sum= ",sum)
def sub():
    sub=a-b
    print("Sub= ",sub)
def mul():
    mul=a*b
    print("Mul= ",mul)
def div():
    div=a/b
    print("Div= ",div)

if operator =='+':
    sum()
elif operator=='-':
    sub()
elif operator=='*':
    mul()
elif operator=='/':
    div()
else:
    print("Not Valid")


