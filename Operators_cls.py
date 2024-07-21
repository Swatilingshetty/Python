#operators:

#values are consider as operands
#symbol will be consider as operator
3+4

#arithmetic operator(+,-,*,%,/,//,**)
#relational or comparison operator(==,!=,<,>,<=,>=)
#logical operator(or,and,not)
#assignment operator(=,+=,-=,*=....)
#membership operator(in,an not)
#identity operator(is, is not)
#bitwise operators(bitwise and(&),bitwise or(!),bitwise xor(^),left shift(<<),right left(>>),bitwise not(~))
#turnary operator

#Datatypes of python
   #Numbers
      #numerical values with or without decimal point
      #a=12,b=4.5
   #Strings
      #Anything which we declare in between" " or ''or ''' '''or""" """..
      #state="karnatak" country="india"
   #lists
      #Sequence of values which are seperated with comma(,) declared inside [ ]..
      #teams=["csr","rcb","mi","kkr",43,5,6,[11,23,45]]
   #Tuples
      #Sequence of values which are seperated with comma(,) declared inside( )...
      #teams=()"csr","rcb","mi","kkr",32,76,9,(6,87,9))
   #Dictionaries
      #Sequence of key:value pair which are seperated with comma(,) declared inside{ }..
      #info={'username':"swati",'password':"password@123",'state':"karnataka",'mobile':6364451583 }
   #sets
      #Sequence of key:value pair which are seperated with comma(,) declared inside{ } which are unoreder and unique..


#Arithimetic operation..
  #+
  #-
  #*

# a=4
# b=4.5
# print(a+b)

# a=5
# b=8.9
# print(a*b)

# str1="python"
# str2="django"
# print(str1+str2)  

# list1=[1,2,3]
# list2=[4,2,6]
# print(list1+list2)

# tuple1=(1,2,3)
# tuple2=(4,5)
# tuple3=tuple1+tuple2
# print(id(tuple1))
# print(id(tuple2))
# print(id(tuple3))

# /, //, %

# 23/5 --4.6

# 5)23(4.6
#   20
#   ----
#    30
#    30
#    ----
#    00

# 23//5  - 4

# 5)23(4.6
#   20
#   ----
#    30
#    30
#    ----
#    00

#  23%5  - 4

#  5)23(4
#    20
#   ---  
#     3

#    346%3 -1

#    3)346(115
#      3
#      -----
#       4
#       3
#       ---
#       16
#       15
#       ---
#        1


# print(23/5)
# print(23//5)
# print(23%5)
# print(346%3)

# ** - exponential or power

# print(3*3)
# print(3**2)
# print(4**5)

#Relational or camparison operator(==,>,<,<=,>=,!=)
# the output of relational operators will be boolean value only..

# print(12==15)
# print(12>15)
# print(12<15)
# print(12<=15)
# print(12>=15)
# print(12!=15)

# print(15==15)
# print(15>16)
# print(15<16)
# print(15<=16)
# print(15>=16)
# print(15!=16)

#ASCII=American standered code for information 

# str1="Python@123"
# str2="django!123"

# print(str1==str2)
# print(str1!=str2)

# print(str1>str2)

# list1=[22,'python',1]
# list2=[22,'django',1]

# print(list1>list2)
# print(list1<list2)

# list3=[23,'python',1]
# list4=[22,24,1]

# print(list3<list4)
# print(list3>list4)

# dict1={'name':'swati'}
# dict2={'email':'suresh@gmail.com'}

# print(dict1>dict2)  #error

# Logical operator(and,or,not):

#BODMAS RULE

# A     B    A and B    A or B    not(A)   not((A or B) and (A and B))
# -----------------------------------------------------------------------
# T     F       F          T        F                   T
# F     T       F          T        T                   T
# T     T       T          T        F                   F
# F     F       F          F        T                   T





# data

# name="balayya"
# slogan="jai balayya"

# #input()- It will help the user to provide the user input
# #defaultly input will take the value as string only..

# name1=input("enter name:")

# print(name)
# print(name1)

# print(type(name1))

# int1 =int(input("enter your value"))  #This will convert string integer into normal integer..

# print(int1)


# print(type(int1))

# int1 =float(input("enter your value"))  

# print(int1)


# print(type(int1))

# int1 =list(input("enter your value:"))  

# print(int1)


# print(type(int1))

#eval - This is for converting the string value into the specific datatype

#  int1 =eval(input("enter your value:"))  

# print(int1)

# print(type(int1))

# name = "balayya"
# slogan = "jai balayya"

# name1 = input("enter name:")
# slogan1 = input("enter slogan:")

# print(name == name1)
# print(slogan==slogan1)

# print(name ==name1 and slogan==slogan1)

# pin=12345
# acc_type="saving"

# pin1=int(input("enter your pin:"))
# acc_type1=input("enter your account type:")

# print(pin==pin1 and acc_type==acc_type1)

# print(pin==pin1 or acc_type==acc_type1)

#Assignment operators:

# a=23
# print(a)
# a=a+3
# print(a)

# a*=4
# print(a)

# a-=2
# print(a)

#membership operators(in,not in):- Output of this also boolean(true/false)

str1 = "Python is a programming language"

# print("python" in str1)

print("a" in str1)

print("angua" in str1 ,"angua" not in str1)

# list1 = [32,'python',3,4,'programming']

# print('python' in list1 ,'python' not in list1) 

# print('p' in list1)

# dict1 = {'name':'swati','email':'swati@gmail.com','city':'karnataka'}

# print('name' in dict1)


# print('swati' in dict1 ,'swati' not in dict1)

# print("city" in dict1)

 