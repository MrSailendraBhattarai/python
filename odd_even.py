
"""num=int(input("Enter any number"))

if(num%2==0):
    print("even")
else:
    print("odd")"""


    #prime number
"""num=int(input("Enter any number"))
start=1
count=0

remainder=num%start
if(remainder==0):
    count+=1
if(start<=num):
    start+=1

if(count>2):
    print("composite")
else:
    print("prime")
    """

n=100
:top
if(n<100):
    print(n)
    if(n%2==0):
        print("even")
    else:
        print("odd")
    goto :top