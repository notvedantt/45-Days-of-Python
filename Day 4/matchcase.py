x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2==0:
        print("x % 2==0 and case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x) #Default case 
#if NO CASE IS MACTHED DEFAULT CASE WILL GET PRINT

#No need to add break statement like c/c++

#OUTPUT
'''
Enter the value of x: 55
55 is not 90

Enter the value of x: 90
90 is not 80
'''