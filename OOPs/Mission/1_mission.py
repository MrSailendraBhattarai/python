import random

class Mission:

    def launch(self):
        a=int(input("What do you want to check:\n1: Check Systems \n2: Check Shields \n3: Check Mission Path \n4: Check Fuel \n5: Check Crew Health\n"))

        def check_systems():
            b=random.randint(1,50)
            if b<20:
                print("Your System Have Problem! ")
            elif b<70:
                print("You need to Repair System: ")
            else:
                print("Your System is in Good Condition: ")
            
        def shields():
            c=random.randint(1,100)
            if c<30:
                print("You need to change Shield! ")
            elif c<70:
                print("You need to Repair Shield: ")
            else:
                print("Shields are Open")
        
        def path():
            d=random.randint(1,10)
            if d<5:
                print("Obstacle Ahead! ")
            else:
                print("Path is Clear. You May Proceed")

        def fuel():
            e=random.randint(1,100)
            print(f"{e}%")
            if e<45:
                print("Low Fuel! Refuel Immediately! ")
            elif e<70:
                print("Fuel is Medium, Keep an Eye on Fuel Levels.")
            else:
                print("Fuel is Full, Everything is Good.")

        def crew_health():
            f=random.randint(1,100)
            if f<20:
                print("Crew Health is Critical! Immediate Medical Attention Required!")
            elif f<60:
                print("Crew Health is Stable.")
            else:
                print("Crew Health is Excellent!")
            
        if a==1:
            check_systems()
        elif a==2:
            shields()  
        elif a==3:
            path()
        elif a==4:
            fuel()
        elif a==5:
            crew_health()

    def monitor_trip(self):
        b=int(input("What do you want to check:\n1: Check Astroid \n2: Check Temperature \n3: Check Communication System \n"))

        def astroid():
            c=random.randint(1,10)
            if c<3:
                print("Asteroid is Coming...")
            elif c<7:
                print("Asteroid is Coming Near...")
            else:
                print("We are going Far from Asteroid: ")
        
        def temperature():
            d=random.randint(1,100)
            print(f"{d} degree")
            if d<30:
                print("Our Vehicle is Safe: ")
            elif d<50:
                print("Open Shield...")
            elif d<80:
                print("Shield is Broken:  ")
            else:
                print("We Are in Danger!")
            
        def communication():
            c=random.randint(1,100)
            if c<30:
                print("Unable to Contact Earth! Try Later.")
            elif c<70:
                print("Contact with Earth Established. All Systems Normal.")
            else:
                print("Communication Link is Strong! Sending Updates.")

        if b==1:
            astroid()  
        elif b==2:
            temperature()
        elif b==3:
            communication()
        else:
            print("Wrong Input: ")

obj = Mission()

while True:
    print("""
    1: Prepare for launch
    2: Trip Monitor
    3: Exit
    """)
    option = input("Enter Option: ")
    if option == '1':
        obj.launch()
    elif option == '2':
        obj.monitor_trip()
    elif option == '3':
        print("Mission Complete. Shutting Down.")
        break
    else:
        print("Invalid Option! Please try again.")
