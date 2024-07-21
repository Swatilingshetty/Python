
# functions:set of line of codes to perform specific task.
# write our logic once use it again and again.

# a=43
# b=54

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# a =14
# b=65

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# function is used for the reusablity of the code..

# syntax of the functions:

# def function_name():
#     statement

# a = 43
# b = 12

# def arithematic_operation():
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# print("heloooooo")
# arithematic_operation()  # function call is mandatory to execute the function..

# print("hiiii")

# a = 16
# b = 6
# arithematic_operation()  # write logic once use it again and again.

# Functions and arguments:

# passing values to the function can be done with 5 different ways:

# 1.positional arguments:
    # accessing the value to the arguments based on the position of values in the function call..

# def employee_details(name,age,company):
    # print(name)
    # print(age)
    # print(comany)
    # print(f"hi {name} your age is {age} and you are working in {company} company...")

# employee_details("sai","21","tcs")

# employee_details("wipro","rajesh","87")

# employee_details("swati",65)  # this will throw an error as we are missing one arguments.


# 2.Default operation:
     # assining the default values to the arguments to the function defination.

# def employee_details(name,company,age=32):
#     print(f"hi {name} your age is {age} and you are working in {company} company...")

# employee_details("sai","wipro")

# 3.Keyword arguments:
     #assinging the value to the arguments based on the keyword of the arguments in the function call..


# 4.arbitary positional arguments:


# def cred_trans(*trans):
#     print(trans)

# cred_trans(4343,3663,783,"hgghhh",7687,9876)   # no.of elements we can add.

# def cred_trans(*trans):
#     print(trans)
#     # amount=0
#     # for ele in trans:
#     #     amount=amount+ele
#     #     print(amount)
#     amount=sum(trans)  
#     print(f"you have done {len(trans)} transaction for an amount of {amount}")

# cred_trans(4343,3663,783,7654,)

# 5.arbitary keyword arguments: passing multiple lenth of keyword arguments..

# def cred_trans(**trans):
#     print(trans)
#     amount=0
#     name=trans.pop('name')
#     email=trans.pop('email')
#     print(name)
#     print(email)
#     print(trans)
#     amount=0
#     for ele in trans:
#         amount=amount+trans[ele]
#         print(f"hi ramesh you have done 3 tranaction for an amount of 3000, the same has sent be sent to ramesh@gmail.com ")

# cred_trans(jan=3213,feb=7654,name="ramesh",email="ramesh@gmail.com")
# cred_trans(mar=9876,apr=5432,may=8765,name="suresh",email="suresh@gmail.com")
# cred_trans(jun=6543,jul=4321,aug=9870,sep=7654,name="mahesh",email="mahesh@gmail.com")

# RETURN : statement which is used to give the response for a function call

# def add(a,b):
# #     print(a+b)
#     return a+b
# add(2,3)

# def sub(a,b,c):
#     return add(a,b) -c

# print(sub(3,4,2))

# def login(username,password):
#     if username=="admin" and password=="admin":
#         return"login successfully"
#     else:
#         return "invalid credentials"
    
# print(login("ramesh","ramesh"))

# def check_cred(username,password):
#     chech=login(username,password)
#     if chech =="login successfully":
#         return "user exist"
#     else:
#         return "invalid user"
    
# print (check_cred("admin","admin"))
