data = [1,2,3,4,5,6]  #[101,102,103,104,105,106]

# #old , using for loop
second_data = []
for number in data:
    second_data.append(number+100)
print(second_data)

#using list comprehension
second_list = [item+100 for item in data]
print(second_list)

#WAP to display even list data using list comprehension
#using loop
data = [1,2,3,4,5,6] 
even_data =  []
for item in data:
    if item%2==0:
        even_data.append(item)

# print(even_data)

#using list comprehension
even_data = [number for number in data if number%2==0]
print(even_data)
