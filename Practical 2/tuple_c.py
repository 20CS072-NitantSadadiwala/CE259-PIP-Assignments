# Nitant Sadadiwala, 20CS072
# Write a Python program to add an item in a tuple
# https://github.com/20CS072-NitantSadadiwala/CE259-PIP-Assignments.git

t = (4, 6, 2, 8, 3, 1)
print(t)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = t + (9,) + (15,)
print(tuplex)
