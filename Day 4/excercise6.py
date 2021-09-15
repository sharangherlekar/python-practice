'''Write a program for ATM ( input 1 = pin,
1. withdraw
2. make a deposit
3. check balance'''

x = int(input("Please enter pin"))
balance = 10000
if x==1234:
   y = int(input("please choose from the following options"
                 "\n1. withdraw"
                 "\n2. Deposit"
                 "\n3. Check balance"))
   if y==1:
       z=int(input("Enter amount to be withdrawn"))
       print(f"you have succesfully withdrawn {z} Rupees")
       bal = balance - z
       print(f"Your current balance is {bal} Rupees")
   elif y==2:
       a = int(input("Enter the amount to be deposited"))
       print(f"you have succesfully deposited {a} Rupees")
       bala = balance - a
       print(f"Your current balance is {bala} Rupees")
   elif y==3:
        print(f"Your current balance is {balance} Rupees")
   else:
       print("please try again")
else:
    print("the pin is invalid")