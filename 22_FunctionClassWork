
# CRUD Operation using Function
print("Welcome!! to My Software\n")
command='y'
students = {}
def add():
    n = int(input("Enter how many students you want to add: "))
    for i in range(n):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        english = float(input("Enter English Mark: "))
        math = float(input("Enter Math Mark: "))
        computer = float(input("Enter Computer Mark: "))

        students[id] = {
        "Name": name,
        "English": english,
        "Math": math,
        "Computer": computer
        }

        print("Student Added Successfully: ")
def search():
    b=int(input("Enter Student ID to Search: "))
    if b in students:
        print(f"Student Found Successfully: {students[b]}")
    else:
        print("Student Not Found: ")
def delete():
    c=int(input("Enter ID to Delete: "))
    if c in students:
        del students[c]
        print("Deleted Successfully: ")
    else:
        print("Student Not Found: ")
def show():
    print(students)
while command=='y':
    a=int(input("Enter any options:\n 1: Add\n 2: Search\n 3: Delete\n 4: Show All Data\n "))
    
    if a==1:
        add()
        
    elif a==2:
        search()

    elif a==3:
        delete()
    elif a==4:
        show()
    else:
        print("Invalid! Enter Between 1-4: ")

    command=input("Do You Want to Continue Y/N: ")
else:
    print("Thank You")