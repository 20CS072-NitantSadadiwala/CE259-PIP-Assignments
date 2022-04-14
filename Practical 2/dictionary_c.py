# Nitant Sadadiwala, 20CS072
# Write a Python program to sum all the items in a dictionary
# https://github.com/20CS072-NitantSadadiwala/CE259-PIP-Assignments.git

def Summation(dict):
    # counter of summation
    sum = 0
    # for loop for iterating values in dictionary
    for i in dict.values():
        sum = sum + i
    return sum

# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300, 'd':500}
print("Sum :", Summation(dict))