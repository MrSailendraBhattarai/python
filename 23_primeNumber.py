# prime number using function

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True  

a = 9
check_prime = is_prime(a)

if check_prime==True:
    print(f"{a} is Prime")
else:
    print(f"{a} is Composite")

