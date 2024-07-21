
# 19/04/24
# Inheritence: A class acquiring the properties of other class..

# single inheritance
# multiple inheritance
# multilevel inheritance
#  hierarchical inheritance 
#  hybrib inheritance


# class parants:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land belongs to {self.name} ."

# obj1=parants("suresh",15)
# print(obj1.property_info())



# class child:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.name} has {self.acres} acres of land."
    
# obj1=child("swati",10)
# print(obj1.property_info())
    
# class first:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres+5

#     def property_info(self):
#         return f"{self.acres} acres of land belongs to {self.name}  "
    
# obj1=first("suresh",15)
# print(obj1.property_info())


# class second(first):
    # def __init__(self, name, acres):
    #     self.name=name
    #     self.acres=acres
    #     super().__init__(name, acres)   #calling the parent class construction.


# MULTIPLE INHERITANCE: a class aquiring the properties of more than one class is called multiple inheritance

# class first:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land belongs to {self.name}  "

# class second:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land registered to {self.name}  "

# class third(first,second):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.name} has {self.acres} acres of land "
    
# obj2=third("ramesh",10)

# print(obj2.property_info())

# multilevel inheritance:

# class first:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

    # def property_info(self):
    #     return f"{self.acres} acres of land belongs to {self.name}  "

# class second(first):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land registered to {self.name}  "

# class third(second):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     # def property_info(self):
    #     return f"{self.name} has {self.acres} acres of land "
    
# obj2=third("ramesh",10)

# print(obj2.property_info())

# HYBRID INHERITANCE: combination of more than one inheritance

# class first:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land belongs to {self.name}  "


# class second(first):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land registered to {self.name}  "


# class third(first):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

    # def property_info(self):
    #     return f"{self.name} has {self.acres} acres of land "
    

# class fourth( third,second):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

# obj2=third("ramesh",10)

# print(obj2.property_info())

# MRO: Method Resolution Order vvimportant in interwiev


# hierarchichal inheritance:more than one class aquiring the properties of a single class is called hierarchical inheritance..

# class first:
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land belongs to {self.name}  "


# class second(first):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

#     def property_info(self):
#         return f"{self.acres} acres of land registered to {self.name}  "


# class third(first):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

    # def property_info(self):
    #     return f"{self.name} has {self.acres} acres of land "
    

# class fourth( third,second):
#     def __init__(self,name,acres):
#         self.name=name
#         self.acres=acres

# obj2=third("ramesh",10)

# print(obj2.property_info())
