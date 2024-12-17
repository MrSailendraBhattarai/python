#make a software which takes user data as input and store students in dictionary and their subjects mark.
#add student
#delete student
#search student
#update student
print("Welcome!! to My Software\n")
command='y'
students = {}
while command=='y':
    a=int(input("Enter any options:\n 1: Add\n 2: Search\n 3: Delete\n 4: Show All Data\n "))
    
    if a==1:

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
    elif a==2:
        b=int(input("Enter Student ID to Search: "))
        if b in students:
            print(f"Student Found Successfully: {students[b]}")
        else:
            print("Student Not Found: ")

    elif a==3:
        c=int(input("Enter ID to Delete: "))
        if c in students:
            del students[c]
            print("Deleted Successfully: ")
        else:
            print("Student Not Found: ")
    elif a==4:
        print(students)
    else:
        print("Invalid! Enter Between 1-4: ")

    command=input("Do You Want to Continue Y/N: ")
else:
    print("Thank You")