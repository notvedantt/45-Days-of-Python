def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) #factorial num - 1 i.e 7*factorial of 6 

print(factorial(3))
#Can add same function in existing function 
