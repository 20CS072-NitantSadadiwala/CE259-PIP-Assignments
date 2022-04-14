print("Enter input string:")
Str = input()
i = 0
j = []
for i in range(len(Str)):
    if Str[i]==Str[i].lower():
     j.append(Str[i].upper())
    else :
        j.append(Str[i].lower())
result = ''.join([str(elem) for elem in j])

print("Result:")
print(result)
