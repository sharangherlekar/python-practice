#username
user = {'sharang' : ['sarang123','acda321@gmail.com',1234567890],'sharley' : ['sarang121','acda322@gmail.com',2234567890]}

while True:
    choice = int(input('1. Sign.'
                       '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ up 2. Sign In 3. Exit'))
    if choice == 1:
        username = input("Username : ")
        password = input("Password : ")
        email = input("Email")
        mobile = input("Number : ")

        if username in user.keys():
            print("Username already exists")
        else:
            for i in user.values():
                if email == i[1]:
                    print("email already exists")
                    break
            else:
                user[username] = [password,email,mobile]
                print("Account has been created")
    elif choice == 2:
        username = input("Username : ")
        password = input("Password : ")

        if username in user.keys():
            for i in user.values():
                if password == i[0]:
                    print('you have logged in')
                    break
            else:
                print('incorrect password')

        else:
            print('incorrect username')
            break
    else:
        break

print(user)