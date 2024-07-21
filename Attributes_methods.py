
# 22/03/24
# Attributes- variables or arguments declared inside the class.
   #instance attributes- attributes which are defined inside the self method and can be ACCESED ANLY with object..
   #class attributes- attributes which are defined inside the class and passed at class declaration and can be accessed with class name and object..

# class employee:

#     name="suresh"

#     def __init__(self,name,mobile) :
#         self.name=name   # instance attributes.
#         self.mobile=mobile  # instance attribute
#         pass            # just for syntax


# obj1=employee("ramesh","63644515843")
# print(obj1.name)
# print(obj1.mobile)

# print(employee.name)

# class attributes can be accesed with class name and object name .name(when we dont have any  instance attributes with the same name )

# Methods : functions defined inside the class..
    # instance methods: methods which are defined inside the class and can be accessed only with object which will take the arguments self..
    # class methods: methods which are defined inside the class and can be accesed with class name and object name which will take the default arguments as cls..
    # static methods : methods which are defined inside the class and can be accessed with class name and object  name...

#  method:
# class employee:
    
#     def __init__(self,name,email):
#         self.name=name
#         pass
    
#     def contact_info(self,mobile):
#       return f"please contact {self.name} at this number..{mobile}"
    
#     def personal_info(self,age,address):
#        return f"{self.name} is { age } years old and lines at {address}"
    
# obj1=employee ("venkat","venkat@gmail.com")

# print(obj1.contact_info("6364451576"))

# print(obj1.personal_info(25,"hyderabad"))

# print(employee.contact_info(obj1,"857656464543"))

# class method:
# class employee:
    
   #  name="suresh"  # class attribute
   #  def __init__(self,name,email):
   #      self.name=name
   #      pass
    
   #  def contact_info(self,mobile):
   #    return f"please contact {self.name} at this number..{mobile}"
    
   #  def personal_info(self,age,address):
   #     return f"{self.name} is {age} years old and lines at{ address}"
    
   #  classmethod
   #  def cls_contact_info(cls,mobile):
   #     return f"please contact {cls.name} at this number {mobile}"
    

# obj1=employee ("venkat","venkat@gmail.com")

# print(obj1.contact_info("6364451576"))

# print(obj1.personal_info(25,"hyderabad"))

# print(employee.contact_info(obj1,"857656464543"))

# Decorator : A decorator is a design pattern in python that allows a user to add new functionality to an existing function or object withouit modifiying the structure .  Decoretors are usually called  before the defination of a function you want to decorate..

# def send_email(email):
#     return f"email sent to {email}"

# print(send_email("swati1234@gmail.com"))

# check_email=send_email

# print(check_email("sagar1234@gmail.com"))

# def func_check_email(func):
#     print(func("swati1234@gmail.com"))

# func_check_email(send_email)