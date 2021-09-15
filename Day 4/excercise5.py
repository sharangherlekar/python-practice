#Write a program for course enquiry(Course name as input - duration of course, fee etc

x = input("Please enter name of course")

if x=="python":
    print("Given below is the information for python course")
    print("Fees = 10000 Rs")
    print("Duration = 3 months")
elif x == "java":
    print("Given below is the information for java course")
    print("Fees = 15000 Rs")
    print ("Duration = 5 months")
else:
    print("Sorry this course is invalid")