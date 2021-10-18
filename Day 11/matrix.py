row = int(input("enter the row size"))
column = int(input("enter the column size"))
matrix = []
for i in range(row):
    matrix.append([])
    for j in range(column):
        matrix[i].append(int(input('enter the element')))
for i in matrix:
    for j in i:
        print(j,end=' ')
    print()

print('')

for i in range(row):
    for j in range(column):
        if i==j or i+j==row-1:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(row):
    for j in range(column):
        if i==0 or i==row-1 or i+j==row-1:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
