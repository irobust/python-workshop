count = 0

def setCount(initialCount=0):
    initialCount += 10
    return initialCount

print(count)
count = setCount(20)
print(count)
