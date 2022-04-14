k = int(input())
room = list(map(int, input().split()))

x = set()
y = set()

for box in room:
    if box not in x:
        x.add(box)
        y.add(box)
    else:
        y.discard(box)

y = list(y)
print(y[0])