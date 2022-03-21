# numbers 1 through 9

x = [i for i in range(10)]
print(x)

y = [i * i for i in range(10)]
print(y)


# multi by 3

list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1]
print(multiplied)

# word manip

ListOfWords = ["this", "is", "a", "list", "of", "words"]

firstlet = [item[0] for item in ListOfWords]
print(firstlet)


list2 = ["A", "B", "C"]

lowerlist = [x.lower() for x in list2]
print(lowerlist)

# adding if

oddeven = [i * i for i in range(5) if i % 2 == 0]
print(oddeven)

string = "Hello 12345 World"

numbers = [i for i in string if i.isnumeric()]
words = [i for i in string if i.isalpha()]
print(words)
print(numbers)


# using a file
myfile = open("test.txt", "r")

result = [i.rstrip("\n") for i in myfile if "line3" in i]
print(result)


def double(x):
    return x * 2


print(double(10))

mynumbers = [double(x) for x in range(10) if x % 2 == 0]
print(mynumbers)


result = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
print(result)
