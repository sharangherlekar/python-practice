#list is dyanamic in nature
#can store any type of value
x = ["python", 20000 , 7.30] #without for loop display 10 times
print(x[1])
print(type(x))
print(20000 in x)
for i in x:
    print(i, end='')
print(" ")
for i in range(len(x)):
    print(i)
x[0] = "java"
print(x)

x.append("PHP")
print(x)
x.insert(2,"hi")
print(x)
x.pop()
print(x)
x.pop(2)
print(x)
x.remove(7.3)
print(x)
print(x.count('java'))
print(x.index('java'))
x.reverse()
print(x)
y = [34,5,6,7]
y.sort()
print(y)
x.extend(y)
print(x)
