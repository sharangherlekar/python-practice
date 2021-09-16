#check if the given pin is valid(if the entered pin is a 4-digit nuber, the pin is valid)

x = int(input("Please enter a pin"))

if 1000<=x>=9999:
    print("The pin is correct")
else:
    print("The pin is incorrect")