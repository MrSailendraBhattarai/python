"""name="kathmandu"
for letter in name:
    full_letter= "@"+letter
    print(full_letter)
"""


animal = ('apple', 'cat', 'dog', 'cow', 'orange')
for letter in animal:
    if letter[0] in 'aeiou': 
        full_name = "An"
    else:
        full_name = "A"
    output = "It is " + full_name + " " + letter
    print(output)

name = "tribhuvanuniversity"
for i in range(18, -1, -1):#reverse string
    print(name[i],end=',')


