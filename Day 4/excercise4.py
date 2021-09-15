#Write a program to convert number to word ( if input is 1 = one, For numbers 1 - 5)
x = int(input("Please enter a number from 1 - 5"))

if   x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
elif x == 5:
    print("five")
else:
    print("Invalid")