#Set= It is a collection which is un-changable, un-Ordered & un-indexed.
eg:-
#Create
set_1={'apple','ball'}

#Delete
set_1.remove('ball')

#Access
for item in set_1:
    print(set_1)

#Add
set_1.add('cat')

set1 = {1,5,7,5}
print(type(set1))
print(set1)


country_first = {"usa","russia","china"}
country_second = {"india","russia","nepal"}

aub = country_first.union(country_second)
aub = country_first | country_second
print(aub)