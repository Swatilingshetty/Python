
# 21/03/24
# oops-object oriented programming

# class: blueprint of an object(detailed descrption of an object)

# object:instance of a class...

# syntax of class
# class:it is the keyword for defining the class.

# class classname:
#     statements


# class employee:
#     name="ramesh"
#     email="ramesh@gmail.com"
#     # mobile=6364451554
#     print(f"{email} is {name} email")

# object creation: calling the class is nothing but object creation..

# obj1=employee()
# print(obj1)
# print(obj1.name)
# print(obj1.email)
# print(employee.name)
# print(employee.email)

# class employee:
#     name="ramesh"
#     email="ramesh@gmail.com"

#     # def display(self):
#     #  name="ramesh"
#     # email="ramesh@gmail.com"

#     def display(self):
#       return f"{self.name} is {self.email} email"
     
#     # print(f"{self.email} is {self.name} email")


# obje1=employee()

# print(obje1.name)
# print(obje1.email)

# print(obje1.display{})

# class employee:
#     name="ramesh"     # class attribute
#     email="ramesh@gmail.com"
#     

#     def display(self):
#      name="ramesh"
#     email="ramesh@gmail.com"
      
#     def display(self,mobile):
#       return f"{self.name} is {self.email} email and {mobile} is the mobile number..."
     
#     # def display(self):
#     #  print(f"{self.email} is {self.name} email")


# obje1=employee()

# print(obje1.name)
# print(obje1.email)
# # print(obje1.mobile)

# print(obje1.display{"65432345654"})


# constructor: __init__- it is a special method which is used to initiate the object.(durder method) ..

# class employee:
    
#     def __init__(self,name,email):
#         self.name=name     # instance attribute
#         self.email=email
#         pass
    
#     def display(self,mobile):
#         return f"{self.name} is {self.email} email and {mobile} is the mobile number"
    
# obj1=employee("swati","swati@gmail.com")

# print(obj1.name)
# print(obj1.email)

# print(obj1.display("765432222"))

# obj2=employee("karan","karan@gmail.com")

# print(obj2.name)
# print(obj2.email)

# print(obj2.display("987654365"))

# attributes: variables inside the class..
      # instance attribut: attributes which are defined inside the self method and can be accessed only with the object ..
         #eg: self.name=name     # instance attribute
            # self.email=email

      # class attribute:attributes which are defined inside the cls and passed at class declaration and  can be accessed only with the name and  object ..
         #eg: name="ramesh"     # class attribute
#             email="ramesh@gmail.com"
   
