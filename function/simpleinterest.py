def simpleinterest():
    p = int(input())
    r = float(input())
    t = int(input())
    print(p*r*t//100)
#simpleinterest()
a = 5
def one():
    x = 12
    print(x+a)

def two():
    one()
    y = 13
    print(y + a)
two()