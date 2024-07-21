# MODULE- every python file

# import - this is the keyword for loading the module..

# import module-name 
       # module - name is nothing but name of the file which we are importing

# import module1_cls    # complete module is imported

# print(module1_cls.name)

# print(module1_cls.add(3,4))

# print(module1_cls.email)

# print(module1_cls.mul(7,6))


# from module-name import functionalities..  2nd syntax

# from module1_cls import * # This will import the all functionalities of the module..

# print(name)

# print(sub(7,6,5))

# print(mul(7,4))


# from module1_cls import name,sub,add

# print(name)

# print(sub(6,5,4))

# print(add(6,5))


# from module1_cls import*
# from module2_cls import*

# print(sub(3,4,5,6))

# from module1_cls import sub as module1_sub
# from module2_cls import sub as module2_sub

# print(module1_sub(3,4,5))

# print(module2_sub(4,5,6,7))

# python will check into 3 locations when we import a modul..
# 1.current diarectory.
# 2.where the python is installed 
# 3.where environment variable is set.

#sys.
# import sys

# print(sys.path)