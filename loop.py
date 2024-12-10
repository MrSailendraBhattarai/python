#While Loop
#For loop

"""for(i=0, i<100, i=i+1):
    print(i)
    #i=i+1"""
#odd/even
"""n=2
while(n<=50):
    if(n%2==0):
        print(f"{n} is Even")
    else:
        print(f"{n} is odd")
    n=n+1"""


#prime number

"""n = 13
count=0
start=1

while(start<=n):
    if n%start == 0:
        count = count + 1
    start = start + 1

if(count<=2):
    print(f"{n} is prime")
else:
    print(f"{n} is composite")
"""


# Python program to display all the prime numbers within an interval

n=int(input("Enter Any Number: "))

print(f"prime number upto {n} are:")

for num in range(2,n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)