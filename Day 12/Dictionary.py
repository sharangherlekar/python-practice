#index reffered to as key
#syntax = key:value.
#key is immutable, value is mutable.
x = {"z":1234 , "a":123}
print(x['a'])
print(min(x))
print(max(x))
#print(x.items())
for i in x.items():
    print(i)
print(x.keys())
print(x.values())
#print(x.popitem())
x.setdefault('b',234)
print(x)
y={1:"one", 2:"Two"}
x.update(y)
print(x)