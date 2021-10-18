#Compute the series, if input is 5 , output should 1,1,2,3,5,8
n = int(input("Enter the range"))
a = 0
b = 1
for i in range(0, n):
    if i <= 1:
        output = i
    else:
        output = a + b
        a = b
        b = output

    print(output)

