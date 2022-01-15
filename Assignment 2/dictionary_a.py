# Nitant Sadadiwala, 20CS072
# Write a Python script to check whether a given key already exists in a dictionary.
# https://github.com/20CS072-NitantSadadiwala/CE259-PIP-Assignments.git

# Function Creation
def checkKey(dict, key):
    # checking condition
    if key in dict.keys():
        print("Present, ", end="")
        print("value =", dict[key])
    else:
        print("Not present")


dict = {'a': 50, 'b': 100, 'c': 150}

key = 'b'
checkKey(dict, key)

key = 'd'
checkKey(dict, key)