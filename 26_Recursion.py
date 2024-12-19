#Wap to print whole number using recursion
def display(n):
    print(n)
    if n<10:
        display(n+1)

display(1)

#wap to print square upto 1-10
def display(n):
    print(n,"^2 ",end='=')
    print(n*n)
    if n<10:
        display(n+1)

display(1)