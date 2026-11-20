myList = []

for i in range(1,101):
    myList.append(i)

print('sum:', sum(myList))
print('min:', min(myList))
print('max:', max(myList))

myList = []

for i in range(1,1001):
    if i%2 != 0:
        myList.append(i)

print('sum:', sum(myList))
print('min:', min(myList))
print('max:', max(myList))
