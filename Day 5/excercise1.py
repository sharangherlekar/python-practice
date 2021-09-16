'''Generate the multiplication table
input = table( n x 1 .... n x 10) [range'''
multi = 1
n = int(input("Enter a number"))

for i in range(1,11,1):
    print(n,'x',i,'=',n * i)
