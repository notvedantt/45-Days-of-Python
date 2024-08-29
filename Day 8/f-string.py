#f-string is available from 3.6 usually used for string formating

#OLD STRING FORMATING
statement = "Hey my name is {0} and I am from {1}"
country = "India"
name ="Vedant"

print(statement.format(name, country))

#NEW METHOD USING F STRING
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}") #Double curly brackets prints values as it is

txt = "For only {price:.2f} dollars"
print(txt.format(price = 19.09999)) #Gives value upto 2 decimal points in float

#OUTPUT
'''
Hey my name is Vedant and I am from India
Hey my name is Vedant and I am from India
Hey my name is {name} and I am from {country}
For only 19.10 dollars
'''