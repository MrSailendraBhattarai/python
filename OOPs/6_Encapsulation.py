# private=It can be only access under same class.
#     eg:
#     __a=10

# protected=it is same like public it can be access from anywhere.
#     eg:
#     _a=5

# public=it can be access outside class.
#     eg:
#     a=5

class BankAccount:
    def __init__(self):
        self.__balance=10 #Private
    
    def _get_amount(self): #Protected
        return self.__balance
    
    def amount(self): #Public
        return self.__balance

obj=BankAccount()
print(obj._get_amount())
print(obj.amount())