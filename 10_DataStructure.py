"""first_list=['apple','ball','shyam',99,'9.3',4.3]#first method to create list
print(first_list[::-1])#reverse

#add item to list append()
first_list.append('cat')
print(first_list)

second_list=list(('apple','ball','cat'))#second method to create list
print(second_list)

#access list item using loop
for item in first_list:
    print(item,end=",")"""


#skip item in list

"""list_1=['apple','ball','cat','ball',5,7,5]
for i in list_1:
    if i== 'ball':
        continue
    print(i)"""


#remove duplicate item from list
"""list_1=['apple','ball','cat','ball',5,7,5]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)"""

#wap to take input from user & add it to list
"""name=input("Enter Your Name: ")
mobile=input("Enter Your Number: ")
address=input("Enter Your Address: ")

list_3=[]

list_3.append(name)
list_3.append(mobile)
list_3.append(address)
print(list_3)"""

#wap to take 5 friends data and store in list
details = []

for i in range(2):
    name = input("Enter Your Name: ")
    mobile = input("Enter Your Number: ")
    address = input("Enter Your Address: ")
    
    total_data = []
    total_data.append(name)
    total_data.append(mobile)
    total_data.append(address)
    
    details.append(total_data)

for i in details:
    print([f"{i[0]},{i[1]},{i[2]}"], end=",")

