#prepare student mark list(ID, marks for 5 subjects as input) output should be total average result
#print suggestion based on student performance
name = (input("Enter your name"))
m = int(input("Enter your maths marks"))
p = int(input("Enter your physics marks"))
c = int(input("Enter your chemistry marks"))

avg = (m + p + c) // 3
print(f"Your average marks is = {avg}")

if avg<=50:
    print(f"{name} please try harder")
elif 50<=avg<=75:
    print(f'{name} you can do better')
elif 75<=avg<=100:
    print(f'{name} good job!')
else:
    print('please enter correct marks')