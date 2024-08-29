import sys

print("Hello, Welcome to the Kon Banega Crorepati")
input("Enter your name: ")

print("Okay let's begin")

#QUESTION 1
Q1 = input("Question 1: 1. What is the capital city of France?\n A)Rome    B)Berlin\n C)Paris    D)Madrid\n").upper()
list1 = ['C', "QUIT"]

if Q1 in list1:
    if Q1 == 'C':
        print("Congratulation you have won 1,000 ruppees")
    elif Q1 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 2
Q2 = input("\n\nQuestion 2: 2. Who wrote the play Romeo and Juliet?\n A)Mark Twain    B)William Shakespeare\n C)Charles Dickens    D)Jane Austen\n").upper()
list2 = ['B', "QUIT"]

if Q2 in list2:
    if Q2 == 'B':
        print("Congratulation you have won 2,000 ruppees")
    elif Q2 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 3
Q3 = input("\n\nQuestion 3: 3. What is the largest planet in our Solar System?\n A)Jupiter    B)Saturn\n C)Earth    D)Mars\n").upper()
list3 = ['A', "QUIT"]

if Q3 in list3:
    if Q3 == 'A':
        print("Congratulation you have won 5,000 ruppees")
    elif Q3 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 4
Q4 = input("\n\nQuestion 4: 4. Which element has the chemical symbol 'O'?\n A)Hydrogen    B)Gold\n C)Oxygen    D)Iron\n").upper()
list4 = ['C', "QUIT"]

if Q4 in list4:
    if Q4 == 'C':
        print("Congratulation you have won 10,000 ruppees")
    elif Q4 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 5
Q5 = input("\n\nQuestion 5: 5. Who painted the Mona Lisa?\n A)Pablo Picasso    B)Vincent van Gogh\n C)Leonardo da Vinci    D)Michelangelo\n").upper()
list5 = ['C', "QUIT"]

if Q5 in list5:
    if Q5 == 'C':
        print("Congratulation you have won 20,000 ruppees")
    elif Q5 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 6
Q6 = input("\n\nQuestion 6: 6. In which year did the Titanic sink?\n A)1912    B)1905\n C)1920    D)1916\n").upper()
list6 = ['A', "QUIT"]

if Q6 in list6:
    if Q6 == 'A':
        print("Congratulation you have won 30,000 ruppees")
    elif Q6 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()
    

#QUESTION 7
Q7 = input("\n\nQuestion 7: 7. Who is G.O.A.T. in football\n A)Ronaldo    B)Messi\n C)Mbappe    D)Benzama\n").upper()
list7 = ['B', "QUIT"]

if Q7 in list7:
    if Q7 == 'B':
        print("Congratulation you have won 50,000 ruppees")
    elif Q7 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 8
Q8 = input("\n\nQuestion 8: 8. What is the hardest natural substance on Earth?\n A)Diamond    B)Gold\n C)Iron    D)Quartz\n").upper()
list8 = ['A', "QUIT"]

if Q8 in list8:
    if Q8 == 'A':
        print("Congratulation you have won 1,00,000 ruppees")
    elif Q8 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 9
Q9 = input("\n\nQuestion 9: 9. What is the capital of Japan?\n A)Tokyo    B)Beiijing\n C)Seoul    D)Bnagkok\n").upper()
list9 = ['A', "QUIT"]

if Q9 in list9:
    if Q9 == 'A':
        print("Congratulation you have won 5,00,000 ruppees")
    elif Q9 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()

#QUESTION 10
Q10 = input("\n\nQuestion 10: 10. Which planet is known as the Red Planet?\n A)Venus    B)Jupiter\n C)Mercury    D)Mars\n").upper()
list10 = ['D', "QUIT"]

if Q10 in list10:
    if Q10 == 'D':
        print("Congratulation you have won 10,00,000 ruppees")
    elif Q10 == 'QUIT':
        print("You chose to quit")
else:
    print("Oh no! your answer is wrong, you lost")
    sys.exit()
