# Write a program to remove duplicate items from the list data = [2, 5, 5, 6, 2]

data=[2,5,5,6,2]
data_1=set(data)
print(data_1)
# How would you find the maximum value in the dictionary {"a": 10, "b": 20, "c": 15}?

n={'a':'10','b':'20','c':'15'}
a=int(n['a'])
b=int(n['b'])
c=int(n['c'])
if a>b and a>c:
    print({a}," is Greater")
elif b>a and b>c:
    print({b}," is Greater")
else:
    print({c}," is Greater")
# Convert the list [1, 2, 3, 4, 5] into a dictionary where the keys are the numbers and the values are their cubes.
list_1=[1,2,3,4,5]
dict_1={}
for i in range(1,6):
    dict_1[i]= i**3
print(dict_1)
# Write a program to skip all numbers divisible by 3 while looping from 1 to 10.
for i in range(0,11):
    if i%3==0:
        continue
    else:
        print(i)
# Write a program to find whether 29 is a prime number or not.
n = 29
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
# Write a program to find the sum of all even numbers between 1 and 50. What will the output be?
i=2
n=0
for i in range(1,51):
    if i%2==0:
        n=n+i
        i=i+1
    else:
        continue
print(n)