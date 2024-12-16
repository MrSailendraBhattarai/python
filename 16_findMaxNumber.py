number_1="329346397819"
x=max(number_1) # Find Maximum Number 
print(x)
y=min(number_1)# find minimum number
print(y)
#find Max Number
highest=0
for n in number_1:
    if int(n) > highest:
        highest=int(n)
print(highest)

#find lowest Number
lowest=0
for n in number_1:
    if int(n) < lowest:
        lowest=int(n)
print(lowest)
