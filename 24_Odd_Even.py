#Odd/Even
def is_even(a):
    if a%2==0:
        return True

a=2
check_even=is_even(a)
if check_even==True:
    print(f"{a} is Even")
else:
    print(f"{a} is Odd")