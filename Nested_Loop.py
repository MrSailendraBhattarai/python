"""for i in ('AB'):
    print(i)
    for j in ('CD'):
        print(j)"""


for i in range (6,1,-1):
    for j in range (i):
        print("*",end='')
    print(" ")

w='abcd'

for i in w:
    print(i)
    for j in w:
        print(i,j)
        for k in w:
            print(i,j,k)
            for l in w:
                print(i,j,k,l)