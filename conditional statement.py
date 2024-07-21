#conditional statements : Those statement which will get executed only when the condition is satisfied

# a=int(input("enter a value:"))

# print(a,"is greaterthan 30")

#If statement :  if the condition is satisfied than the statements inside the if block get executed..

#induntation: the space before the statements is called induntation.

# if condition:
#     statements
# a=50
# if a>40:
#     print(a,"is greaterthan 40")

# b=20
# if b>20:
#     print(b,"is greater than 20")
# if a>30:
#     print(a,"is greaterthan 30")

# print(a,"is lessthan 30")

# if-else statement: if the condition is satisfied than the statement inside the if block will get executed

# if condition:
#     statement
# else:
#     statement

# a=30
# if a>30:
#     print(a,"is greaterthan 30"),
# else:
#    print(a,"is lessthan 30")

# if-elif-else statement: if the condition is satisfied than the statements inside the if blocks will get executed otherwise the condition inside the elif block will get executed if the condition is satisfied than the statements inside the elif block will get executed otherwise the statements inside the else block will get executed

# if condition:
#     statements
# elif condition:
#     statements
# else:

# without if statement we can't use elif   
a=20
if a>30:
    print(a,"isgreaterthan 30")
elif a==30:
    print(a,"is equal to 30")
elif a==20 and a%2==0:
    print(a,"is equal to 20 and even")
else:
    print(a,"is lessthan 30")


# hero1= input("enter hero name:")
# movie_name = input("enter movie name:")
# if hero1=="balayya":
#     print("balayya is a legend")
# else:
#     print("hero not matched")

# if hero1 == "balayya" and movie_name=="legend":
#     print("balayya is a legend")
# else:
#     print("details not matched")

# print("thank you for using our application")

# if-elif-else statement : if the condition is true then the statements inside the if block will be executed otherwise the statements inside elif block will be executed
    
#     else statement is optional.
#     if should be declared for sure before declaring the elif statement.


# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# percentage=int(input("enter your percentage:"))

# if percentage>=70:
#     print("you got distraction")
# elif percentage>=60 and percentage<70:
#     print("you got first class")
# elif percentage>=50 and percentage<60:
#     print("you got second class")
# elif percentage>=40 and percentage<50:
#     print("you got third class")
# else:
#     print("you are disqualified")

# hero_name = input("enter hero name:")

# if hero_name == 'chiru':
#     print("mokka kada ani peekestha peeka kostha")
# elif hero_name == 'venky':
#     print("single hand ganesh")
# else:
#     print("hero not matched")

# pin1 check:
#      account type check:
#         amount asking:
#             print(ammount withdrawed)
#      account type error
# pin1 incorect error 

# NESTED CONDITIONALS: 
    # writnig conditional statements inside the conditional statements.

# if condition:
#     if condition:
#         statement
#     elif condition:
#         statements
#     else:
#         statements
# elif condition:
#     if condition:
#         statements
#     elif condition:
#         statements
#     else:
#         statements

# hero_name = input("enter hero name")
# movie_name =input("enter movie name")
# if hero_name == 'chiru':
#     if movie_name == 'indar':
#         print("nuvu nanne kottara")
#     elif movie_name =='bhupathi':
#         print("im waitinggggggg")
#     else:
#         print("movie name not matched")

# elif hero_name == "balayya":
#     if movie_name == "legend":
#         print("thuuu thaaa nghkjbjhfbf")
#     elif movie_name =='simha':
#         print("kjhkudfjhguyrwgfr")
#     else:
#         print("movie name not matched")
# else:
#     print("hero not matched")

# turnary operator : it is a conditional operator which is used to design the volumes based on the condition

# statement1 if condition else statement2

# a= 20
# if a>10:
#     print("a is greater than 10")
#     a+=1
#     print(a)
# else:
#      print("a is lessthan 10")

# print("a is greater than10") if a>10 else print("a is less than 10")

# if condition:
#      statement
     
# list1=[12,13,54,"python","dsa",7,54]

# for ele in list1:
#     print(list1[3])