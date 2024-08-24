def average1(a,b): #Required arguments
    print("Average is", (a+b)/2)
average1(5,10)

def average2(a=2,b=4): #Defaultarguments
    print("Average is", (a+b)/2)
average2(5,10) #Default values are skiiped and user values are executed
average2(3) #Single value refers to "a"" with given b=4
average2(b=8) #a and user given b are executed

average2(b=10, a=5) #Order doenst matter in KEYWORD argument

def average3(*numbers): #Argument taken as tuple
    sum = 0
    for i in numbers:
        sum = sum + 1
    print("Average is: ", sum/ len(numbers))
