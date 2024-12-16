#swap value of a & b
a=5
b=9
print("Before Swap A: ",a)
print("Berore Swap B: ",b)

temp=a
a=b #swap value using temp variable
b=temp

a,b=b,a#swap value without using temp variable
print("After Swap A: ",a)
print("After Swap B: ",b)


# Square of Every items in list
#list_1.clear() clear all the data
#data.remove() remove specific data from list
#list_1=list_2.copy() copy all data to list_1
list_1=[2,5,6,7,3]
for i in list_1:
    square=i*i
    list_2=[]
    list_2.append(square)

    print(list_2,end=',')