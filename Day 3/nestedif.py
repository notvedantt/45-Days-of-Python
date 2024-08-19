num = int(input("Enter your number: "))
print("Your number is", num)

if(num<0):
    print("Number is neagtive.")
elif(num>0):
    if(num <= 10):
        print("Number is between 0 to 10")
    elif(num > 10 and num <= 20):
        print("Number is between 10 to 20")
    else:
        print("Number is greater athan 20")
else:
    print("Number is zero")
        


#OUTPUT
'''
1. Enter your number: 0
Your number is 0
Number is zero

2.Enter your number: 8
Your number is 8
Number is between 0 to 10

3.Enter your number: 16
Your number is 16
Number is between 10 to 20

4.Enter your number: 78
Your number is 78
Number is greater athan 20
'''