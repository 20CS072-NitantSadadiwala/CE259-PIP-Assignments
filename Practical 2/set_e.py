# Nitant Sadadiwala, 20CS072
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# https://github.com/20CS072-NitantSadadiwala/CE259-PIP-Assignments.git

from collections import Counter
s = 'qwertyytrewqnitant'
print("Original string: "+s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3))