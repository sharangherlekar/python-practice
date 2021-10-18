#get 2 values from the user
#digits in both input if it is equal, addtion else subtract

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
a = x -y
b = x + y
if x>=0 and x<=9:
    if y>=0 and y<=9:
        print(b)
    else:
        print(a)
elif x>=10 and x<=99:
    if y>=10 and y<=99:
        print(b)
    else:
        print(a)
elif x>=100 and x<=999:
    if y>=100 and y<=999:
        print(b)
    else:
        print(a)


else:

    print("invalid")
