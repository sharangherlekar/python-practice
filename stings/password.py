

n = input("Enter a password")
alpha = 0
numb = 0
spec = 0

for i in n:

    i = ord(i)
    print(i, end="")
    if i>=ord('a') and i<=ord('z'):
        alpha += 1
    elif i>=ord("0") and i<=ord('9'):
        numb += 1
    else:
        spec += 1
print(alpha)
if alpha>=1:
    print("weak")
elif alpha>=1 and numb>=1:
    print("strong")
else:
    print("very strong")

