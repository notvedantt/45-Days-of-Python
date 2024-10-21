def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) #factorial num - 1 i.e 7*factorial of 6 

print(factorial(7))


def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n>1):
        return (fibonacci(n-1) + fibonacci(n-2)) #Can add same function in existing function 
    
print(fibonacci(7))


