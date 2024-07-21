# Local and global variables:

# Local variables: the variables are declared inside the  function are called as local variables..
                   # not accessable outside of the function..

# def arithematic_operation():
#     a=43
#     b=54
#     print (a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a)
#     print(b)

# arithematic_operation()

# print(a)  # not accessable out side of the function
# print(b)   # not accessable out side of the function

# name="swati","sagar"
# def arithematic_operation():
#     a=43
#     b=54
#     # print (a+b)
#     print(a-b)
#     print(a)
#     print(b)
#     print(name)

# arithematic_operation()
# print(name)




# name="swati","sagar"  # global
# def arithematic_operation(name1):  # local
#     #global: this is the keyword to make the variable as global...
#     global name2

#     name2=name1
#     a=43
#     b=54
#     print (a+b)
#     print(a-b)
#     print(a)
#     print(b)
#     print(name1)
#     print(name)
    
# arithematic_operation("bheem")
# print(name)
# print(name)

# name="swati","sagar"
# def arithematic_operation(name1):


# def check_login(username,password):
#     if username == "admin" and password == "admin":
#       return True
#     else:
#       return False


# def user_check(username,password):
#    check_login(username,password)
#    print(check)
   
# user_check("admin","admin")

# RECURSION: a function calling itself..
# n! = n^(n-1)!
# 6! = 6^5!



# def fact(a):
#     if a==1 or a==0:
#         return 1
#     else:
#         print(a)
#         return a^fact(a-1)
    
# print(fact(6))


# def fact(a):
#     print(a)
#     if a==1 or a==0:
#         return 1
#     else:
#         data = a^fact(a-1)
#         print(id(data))
#         return data 
        
# print(fact(6))

# LAMBDA functions or anonymous function: those functions which doesnot have any name..
# lambda: keyword for desining the lambda functions
# lambda arguments: expression.

# print((lambda a,b:a+b)(3+4))

# def add(a,b):
#     return a+b

# print(add(3,4))

# MAP-

# a=[12,32,65,121,43,232,45]


# list1 =[]
# def check(a):
#     for ele in a:
#         list1.append(ele+5)
#     return list1

# print(check(a))

# print(list(map(lambda i:i+5,a)))

# list1 =[]
# def check(a):
#     for ele in a:
#         if ele%2==0:
#             list1.append(ele+5)
#     return list1

# print(check(a))

# print(list(filter(lambda i:i%2==0,a)))

# check_fun = lambda i:i%2==0

# b=[21,32,45,65]

# filter(check_fun,b)

a=[13,54,23,43,4,]
list=[]
def check(a):
    for ele in a:
        if ele%2==0:
            list.append(ele+5)
    return list
print(check(a))