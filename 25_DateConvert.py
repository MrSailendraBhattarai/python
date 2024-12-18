def Bs_Ad(a, b, c):
    
    a = a - 57  
    b = b + 3   
    c = c + 15  
    
    
    Ad = (f"AD Year: {a}, Month: {b}, Day: {c}")
    print(Ad)

def Ad_Bs(a, b, c):
    
    a = a + 57  
    b = b - 3   
    c = c - 15  
    
    
    Bs = (f"Bs Year: {a}, Month: {b}, Day: {c}")
    print(Bs)


n = int(input("Enter Options \n 1: BS to AD \n 2: AD to BS \n"))

if n == 1:
    Year = int(input("Enter Year: "))
    Month = int(input("Enter Month: "))
    Day = int(input("Enter Day: "))
    
    Bs_Ad(Year, Month, Day)

elif n == 2:
    Year = int(input("Enter Year: "))
    Month = int(input("Enter Month: "))
    Day = int(input("Enter Day: "))
    
    Ad_Bs(Year, Month, Day)

else:
    print("Invalid! ")

