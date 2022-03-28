""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""


listyboi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = list(filter(lambda n: (n % 2 == 0), listyboi))
print(output)
output = list(filter(lambda n: (n % 2 == 1), listyboi))
print(output)


""" 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

output = list(filter(lambda n: (len(n) == 6), weekdays))
print(output)


""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""
OGList = ["orange", "red", "green", "blue", "white", "black"]
output = list(filter(lambda n: ("a" not in n), OGList))
print(output)

""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
output = list(filter(lambda n: (n not in list2), list1))
print(output)


""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""

OGList = ["red", "black", "white", "green", "orange"]
search = "ack"
output = list(filter(lambda n: (search in n), OGList))
print(output)
search = "abc"
output = list(filter(lambda n: (search in n), OGList))
print(output)

""" 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""
x = input("what's the password?")
# what??????
isupperletter = lambda n: n.isupper()
islowerletter = lambda n: n.islower()
isnumber = lambda n: n in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("is that a valid password? let's findout")
print(
    any(filter(isupperletter, x))
    == any(filter(islowerletter, x))
    == any(filter(isnumber, x))
    == (7 <= len(x))
    == True
)

""" 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
original_scores = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Social sciences", 82),
]

ordered_scores = sorted(original_scores, key=lambda x: x[1])
print(ordered_scores)
