marks = [3, 5, 6, "Investment", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

#Same thing applies for strings as well!
if "In" in "Investment":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

#OUTPUT
'''
[3, 5, 6, 'Investment', True, 6, 7, 2, 32, 345, 23]
<class 'list'>
3
5
6
Investment
True
6
32
32
6
6
No
Yes
[3, 5, 6, 'Investment', True, 6, 7]
[5, 6, 'Investment', True, 6, 7, 2, 32]
[5, True, 2]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]

'''