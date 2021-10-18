#Tuple is Immutable
# count and index only available
x = 3,4,5
#or x = (3,4,5)
print(len(x))
print(max(x))
print(min(x))
y = list(x)
print(y)
print(x)
for i in x:
    print(i,end =" ")
print('')
print(x.count(7))
print(x.index(3))