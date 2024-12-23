Dictionary= It is a mutable data structure which allow to store key & value pairs.
eg:-
Create
Dict_1={'1':'Apple','2':'Ball'}

Delete
del Dict_1[1]

Access
for 2 in Dict_1:
    print(Dict_1[2])

Add 
Dict_1[3]={
'Cat'
}

#Add +977 to mobile
user_data_detail ={'name':'Skill Shikshya','location':'KTM','mobile':'98080'}
#print(user_data_detail['name'])
for key in user_data_detail:
    if(key=='mobile'):
        user_data_detail[key] = "+977-"+ user_data_detail[key]
        
print(user_data_detail)