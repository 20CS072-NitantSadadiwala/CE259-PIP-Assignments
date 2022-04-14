try:
    a = [10, 20, 30]
    print (a[3])
except LookupError:
    print ("Index out of bound error")