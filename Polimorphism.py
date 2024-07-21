
# 23/04/24
# Polimorphism: multiple,form(ways)

# method overriding:
# method overloading:

# class father:
#     email="swati@gmail.com"

#     def send_email(self):
#         return f"email has been sent to {self.email}"
    
# class child(father):
#     email="swatichild@gmail.com"

#     def send_email(self):
#         return f"email will be sent soon to {self .email}"
    
# obj1=child()

# print(obj1.send_email())

# class father:
#     email="sagar@gmail.com"

#     def recieve_email(self):
#        return f"email has been recieve from {self.email}"
    
# obj1=father()
# print(obj1.recieve_email())


# class child:
#     email="sagar112@gmail.com"

#     def recieve_email(self):
#         return f"email will be get soon to {self.email}"
    
# obj1=child()

# print(obj1.recieve_email())



# method overloading: considering the method based on the no.of arguments passed to the methods.
# but python doesnot support the concept of method overloading ..

# class child:
    
#     def trans(self,tran1,tran2):
#         return tran1+tran2
    
#     def trans(self,tran1,tran2,tran3):
#         return tran1+tran2+tran3
    
# obj1=child()

## print(obj1.trans(2000,3000))

# print(obj1.trans(2000,1000,3000))

# class child:
    
#     def cred(self,tran1,tran2,):
#         return tran2+tran1
    
#     def cred(self,tran1,tran2,tran3):
#         return tran1+tran2+tran3
    
# obj1=child()
# # print(obj1.cred(200,322))

# print(obj1.cred(300,400,500))