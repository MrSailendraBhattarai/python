
a="ram"
b="9"
print(a+str(b))#concat string

first="   Hello   "
print(first.strip()) # remove whitespace

skill="skillshikshaya@gmail.com"
splitted_data=skill.split('@') # to divide words
print(splitted_data)

about_nepal="nepal is .......qjjsajsj...alkskjsjdjs.india"

correct=about_nepal.replace('india','nepal')#replace words
print(correct)

father_name="some name"
print(father_name.upper())#all uppercase
print(father_name.capitalize())#first word first letter capital
print(father_name.title())#all word first letter capital



a= "abcdefghijklaa"
print(a.casefold())# lowercase
print(a.count("a"))#count all words
print(a.find("i"))#find words available in strings
print(a.endswith("laa"))#find last word of string
print(len(a))#find length of string
print(a.islower())#Returns True if all characters in the string are lower case
print(a.startswith("b"))#Returns true if the string starts with the specified value
print(a.index("g"))#Searches the string for a specified value and returns the position of where it was found
print(a.center(30,"*"))#Returns a centered string
print(a.isalnum())#Returns True if all characters in the string are alphanumeric