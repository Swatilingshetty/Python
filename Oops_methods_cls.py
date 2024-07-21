
# 15/04/2024
# methods: functions modified inside a class are called methods.

# Python classes has 3 types of methods:
# 1.instance methods
# 2.class methods
# 3.static methods

# instance methods:those methods which contain self as first arguments and can be accessed only with object..

# class employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
        # self.pay=pay

    # instance method:
#     def emp_fullname(self):
#         return f"{self.first} {self.last}"
    
# obj1=employee("ramesh","kumar",50000)
# print(obj1.emp_fullname())

# emp2=employee("swati","lingshetty",30000)
# print(emp2.emp_fullname())

# class employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay

#     # instance method:
#     def emp_fullname(self):
#         return f"{self.first} {self.last}"
    
#     def emp_salary(self):
#         return f"{self.emp_fullname()}'s salary is {self.pay}"
    

# obj1=employee("ramesh","kumar",50000)
# print(obj1.emp_fullname())
# print(obj1.emp_salary())

# print(employee.emp_fullname())  # its not possible with class..  instance method accessed only with thw object..

# Class method: those methods which contain cls as first argument and can be accessed with both class and object..

# class employee:
#     first="mahesh"
#     last="rao"
#     def __init__(self,first,last,pay):
#         pass
#         self.first=first
#         self.last=last
#         self.pay=pay

#     # instance method:
#     def emp_fullname(self):
#         return f"{self.first} {self.last}"
    
#     def emp_salary(self):
#         return f"{self.emp_fullname()}'s salary is {self.pay}"
    
#     # class method
#     @classmethod
#     def cls_emp_fullname(cls,first,last):
#         return f"{cls.first} {cls.last}"

# obj1=employee("swati","lingshetty",30000)

# print(obj1.emp_fullname())

# # print(obj1.emp_salary())

# print(obj1.cls_emp_fullname("suresh","kumar"))

#DECORATORS: Decorators are used to modift the bahavior of functions or methods.

# check_session-15 lines 


# login=username,password
# balance=logout, api/balance
# transfer=api/transfer

# bill-pay=api/bill-pay

# def email_valid(email):
#     return email.lower()

# function is being based as an object..

# dummy_email=email_valid("SWATi@GMAIL.com")
# print(dummy_email)

# passing function as an arguments to other function..
# def email_valid(email):
#     return email.lower()

# def convert_email(email):
#     return email.upper()

# def dummy_email(function):
#     return function("JHGFGH@JHGF.COM")

# # def dummy_email(funct):
# #     return funct("gfdsgfd@hgfdgf.com")

# print(dummy_email(email_valid))

# print(dummy_email(convert_email))

# 18/04/2024

# def email_valid(email):
#     return email.lower()

# def get_email(email):
#     return email_valid(email)

# print(get_email("DSGFDJF@jhhGJ.Com"))

# def email_valid(funct):      # this is the logic which i want to use multiple times.
#     def inner(arg1):
#         arg1=arg1.lower()
#         # arg1=arg1.upper()
#         return funct(arg1)
#     return inner

# def get_email(email):
#     return email

# get_email=email_valid(get_email)

# print(get_email("DSGFDJF@jhhGJ.Com"))

# print(get_email("fggfg@ghgh.com"))

class employee:

    def __init__(self):
        pass

    def cls_full_name(cls,first_name,last_name):
        return first_name+last_name
    
    def cls_email(cls,email):
        return cls.cls_full_name()+"email has been sent to {email}"
    
obj1=employee()

print(obj1.cls_full_name{"sanjana"."reddy"})

print(obj1.cls_email("fggfg@ghgh.com"))

