# 1) Countdown
myArray = []
def countdown(num):
    for i in range(num, -1, -1):
        num = i 
        myArray.append(num)
    return myArray

print(countdown(5))

# 2) Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def print_and_return(a,b):
    print(a)
    return b

print(print_and_return(2,5)) 

# this is what i originally came up with, but it doesn't take a list. Only after checkin the solutions file i saw that you can add 'List' in as a paramater of a function
# adding solution file answer as well for further clarification below 
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([2,5]))

# 3) First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

sum = 0 
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([5,2,3,3,5]))

# 4) Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

newArray = []
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    for i in range(0,len(list)):
        if list[i] > list[1]:
            newArray.append(list[i])
    print(len(newArray))
    return newArray

print(values_greater_than_second([1,2,3,1,4,1,5]))
print(values_greater_than_second([2]))

# 5) This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def length_and_value(size, value):
    myList = []
    for i in range(0, size):
        myList.append(value)
    return myList

print(length_and_value(4,7))
print(length_and_value(5, 59))