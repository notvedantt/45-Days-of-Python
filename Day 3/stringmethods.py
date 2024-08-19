#Strings are immutable
#Upper and Lower
str1 = "HOndA"
print(str1.upper()) #Converts string into upper case
print(str1.lower()) #Converts string into lower case

#Strip
str2 = "Hello !!"
print(str2.rstrip("!")) #Removes any trailing characters

#Replace and split
str3 = "Silver spoon"
print(str3.replace("Silver", "Gold")) #Replaces characters within the string
print(str3.split(" ")) #Seperates with a white space

#Capitalize and centre
str4 = "introduction to PyThon"
print(str4.capitalize()) #Capitalizes first letter and lower case all others
print(str4.center(40)) #Moves the string 40 space from the beginning
 
#Count, endswith , startswith
print(str3.count("s")) #Counts ahe the number value in the string
print(str2.endswith("!!")) #Checks the string for ending with given value and answer's in true or false
print(str2.startswith("H")) #Checks the string for starting with given value and answer's in true or false
 
#Difference between find and index methods
print(str4.find("to")) #Finds first occurence of given value in the string
print(str4.find("too")) #IF value doesnt exist it returns output as (-1)
#print(str4.index("too")) IF value doesnt exist it returns valueerror 

#isalnum, isalpha, islower
str5 = "Welcometotheclub"
print(str5.isalnum()) #If entire string consists of alphanumric value it returns TRue else False
print(str5.isalpha()) #If entire string consists of alphabet it returns TRue else False
print(str5.islower()) #If entire string consists of lower case values it returns TRue else False

#isprintable and isspace
str6 = "Happy Birthday"
print(str6.isprintable()) #Return true is value is printable else false
print(str6.isspace()) #Returns true if string contains whitespace

#istitle and swapcase
str7 = "World Health Organization"
print(str7.istitle()) #Returns true if every word has starting letter capital in a given string
print(str7.swapcase()) #Inerchanges upper case to lower case and vice versa

print(str4.title()) # Converts string to title string



#OUTPUT
'''
HONDA
honda
Hello 
Gold spoon
['Silver', 'spoon']
Introduction to python
         introduction to PyThon
1
True
True
13
-1
True
True
False
True
False
True
wORLD hEALTH oRGANIZATION
Introduction To Python
'''








