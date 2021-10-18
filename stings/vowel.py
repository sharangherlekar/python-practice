a = input("enter a string")
if (a[0] == 'A' or a[0] == 'a'
    or a[0] == 'E' or a[0] == 'e'
    or a[0] == 'I' or a[0] == 'i'
    or a[0] == 'O' or a[0] == 'o'
    or a[0] == 'U' or a[0] == 'u'):
        if ( a[-1] == 'A' or a[-1] == 'a'
            or a[-1] == 'E' or a[-1] == 'e'
            or a[-1] == 'I' or a[-1] == 'i'
            or a[-1] == 'O' or a[-1] == 'o'
            or a[-1] == 'U' or a[-1] == 'u'):
            print('the string starts and ends with a vowel')
        else:
            print("the string does not start and end with a vowel")
else:
    print('does not start and end with a vowel')