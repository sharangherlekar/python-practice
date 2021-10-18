#employee pay slip(employee id, name , basic pay) final = net salary

name = input("enter your name")
id = int(input("Enter your employee id"))
basicpay = int(input("Enter your basic pay"))
allowance = 5000

netsalary = basicpay + allowance
print(" ")
print(f"name :{name} ")
print(f"id : {id}")
print(f"basicpay : {basicpay}")
print(f"net salary = {netsalary}")