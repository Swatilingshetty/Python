
#strings : sequence of charecters declared using single quotes or double quotes or triple quotes..

# str1 = 'python is a programming language'
# str2 = "python is a programming language"
# str3 = """python is a programming language"""

# print(str1)

# print(str2)

# print(str3)

# print(type(str1))

# print(type(str2))

# print(type(str3))

# single line strings : declared using single quotes or double quotes..

# str1 = 'python is a programming language
# django is a web frameworks'

# str2 = "python is a programming language
# django is a web frameworks"

#multi line strings : declared using triangle quotes..

# str3 = """python is a programming language
# django is a web frameworks"""

# print(str3)

# print(type(str3))

# str1 = 'twinkle twinkle' little star' - no valid syntax as starting with single quote and got single quote..

# str2 = "twinkle twinkle' little star"

# print(str2)

# str2 = 'twinkle twinkle" little star'

# print(str2)
# print(type(str2))

# str2 = """twinkle twinkle' "little star"""
# print(str2)
# print(type(str2))

#accessing the charecters from string.. - indexing

# indexing : accessing the elements to the sequence is done with indexing 

# indexing will start from 0..

# [ ]- we use this to access the indexing.

# str1 = "python is a programming language"

# print(str1[0])

# print(str1[14])

# print(str1[3:15]) # it will take from 3 to 14

# print(str1[3:23:3])

# negative indexing : performing the indexing reverse order

# print(str1[-1])

# print(str1[-2:-15:-4])

# print(len(str1))
# print(str1[-1:-33:-1]) # or

# print(str1[::-1])

# print(str1[::-7])

# reverse_str1 = str1[::-1]

# print(str1)

# print(reverse_str1)

# print(id(str1))

# print(id(reverse_str1))

#strings are immutable - we cannot change the value of the strings

# str1 = "django framework"
# str1 = "python is a programming language"
# print(str1)

# basic operations on strings
# cancatination(+) : adding 2 strings and making it as single string..
# Repetation(*) : reapiting the string for n number of times..

# str1 = "python" 
# str2 = "django"
# print(str1+str2)

# print(str1)
# print(str2)

# str3 = str1+str2
# print(str3)

# str2 = "django"
# print(str2*4)

#strings methods : built in methods which are used to perform some operation on strings..
# print(dir(str))

#startswith() : it will check wheather the main string is starting with the substring or not..

# str1 = "Django is a web framework"
# print(str1.startswith('django'))
# print(str1.startswith('Dj'))

# # endswith() : it will check wheather the main string is ending with the substring or not.

# str1 = "python ia a programming language"
# print(str1.endswith('language'))
# print(str1.endswith('LANGAUGE'))

# isalpha()- its to check weather everything inside the string is alphabets or not..

# name = "Bheem Hulsoore"
# print(name.isalpha())

# # isalnum() : its to check wheather everything inside the string is alphabets.

# username = "Bheem123"
# # username1 = "123"
# # username2 = "Bheem"
# # print(username.isalnum())
# # print(username1.isalnum())
# # print(username2.isalnum())

# print(username[1:7].isalnum())

# print(len(name))

# print(id(name))

# its for just checking weather everything inside the string is numbers only..

# mobile = "45678901234567"

# print(mobile.isdigit())


# mobile = "456789 01234567"

# print(mobile.isdigit())

#islower() : it is to check weather all the alphabets inside the string or lowercase or not
#isupper() : it is to check weather all the alphabets inside the string or uppercase or not

# email = "bheem.12@gmail.com"

# print(email.islower())

# email = "bheem.12@gmail.COM"

# print(email.islower())

# email = "bheem.12@gmail.com"

# print(email.isupper())

# email = "BHEEM.12@GMAIL.COM"

# print(email.isupper())

# email = "bheem.12@gmail.COM"

# print(email.lower())
# print(email.upper())

#title() : it will convert the string into title format
#capitalize() : it will convert the string into capitalised format
#swapcase() : it will convert lower to upper and vice versa.

# quote = "Twinkle TwiNKLE little star"
# print(quote.title())

# print(quote.capitalize())

# print(quote.swapcase())

#index() : it is used find the index value of the element inside the string..
# quote = "Twinkle TwiNKLE little star"
# print(quote.index('e'))
# print(quote.index('inkle'))
# print(quote.index('le'))

#find() : it is used to find the index value of the element inside the string
# quote = "Twinkle TwiNKLE little star"
# print(quote.find('inkle'))
# print(quote.find('le'))
# print(quote.find('e'))

# # if 'z' in quote:
# #     print(quote.index('z'))

# print(quote.find('z'))

# # when the element is notpresent,index will throw the error and stop program execution.
# # but find will return the output as -1..

# # count() : it will return how many times a substring is reoeated inside the main string.

# print(quote.count('e'))
# print(quote.count('z'))
# print(quote.count('t'))

#split(): it will devide the string into multiple string and will returns the output as list..
# by default spliitting will be performed on space()..
# if we specific any substring it will do the split based on the substring..

# str1="python is a programming language"

# print(str1.split())

# print(str1.split('a'))

# print(str1.split('g'))

# print(str1.split('z'))

# strip() : by default it is used to remove the escape sequence at the starting and ending of the string..
# \n - newline
# \t - tabspace

# s
#str1="\npython\t programming \nlanguage\n"

# print(str1)

# print(str1.strip())

# 1srtrip : performing the strip operation at the starting of the string..

# print(str1.lstrip())

# print(str1.rstrip())

#replace() :it for replacing the substring with someother substring inside the main string..

# dialogue = "Dont trouble the trouble if you trouble the trouble trouble trouble you i am not the trouble i am the truth."

# print(dialogue.replace('trouble','problem'))

# print(dialogue.replace('the','d'))

# print(dialogue.replace('trouble','problem',3))

#zfill() : Zero fills.. zfill will perform the operation only lenth of our string is less 

# id1 ="B2150523"

# print(id1.zfill(10))

# id2 = "B1234567895"

# print(id2.zfill(10))

#join() : its for joining a charecter for every charecter inside the string..

# str1="python"

# print("@".join(str1))

# list1 = ["python","is","a","programming","language"]

# print("".join(list1))

# print(" ".join(list1))

# data = ""
# for ele in list1:  # in ele place we can take any charecter like a,ab,bg,ngds..
#     data=data+" "+ele

# print(data.strip())

# .format() : its for framing the strings..

# message ="use this OTP 647564 for your recent purchase at amazon. for an account of RS.756/-"

# message1 ="use this is OTP {} for your recent purchase at {} for an amount of RS.{}/-".format(647474,'flipkart.com',6574)

# print(message1)

# message2 ="use this is OTP {} for your recent purchase at {} for an amount of RS.{}/-".format(123456,'myntra.com',8888)

# print(message2)

# otp =input("enter OTP:")
# website =input("enter website:")
# amount =input("enter amount:")

# message1 ="use this is OTP {} for your recent purchase at {} for an amount of RS.{}/-".format(otp,website,amount)

# print(message1)

# message1 =f"use this is  {otp} for your recent purchase at {website} for an amount of RS.{amount}/-"

# print(message1)

# str1 = "python is a programming language"

# print(str1.index('a'))

# enter your charecter : 'a'
    # condition if the charecter percent inside the main string
        #enter which occurance : 6
            # condition to check wheather  charecter occured that many times or not??
                # print the index of that occurance
            # charecter has been occured only 4 times,try lesser.
# charecter is not present in the string..


# TASK1 = ATM task

# pin1 = int(input('enter your pin:')) #'1234'

# if pin1 == 1234:
#     account_type = input("enter your account type")
#     if account_type =="saving":
#         amount = input("enter amount to withdrwal:")
#         print(amount,"is debited from your account.")
#     else:
#         print("account type doesnot match")
# else:
#     print("invalid pin")

#TASK2 = making the user for 3 times.

# check = True
# count = 0
# while check:
#     pin1 = int(input('enter your pin:')) #'1234'

# if pin1 == 1234:
#     account_type = input("enter your account type")
#     if account_type =="saving":
#         amount = input("enter amount to withdrwal:")
#         print(amount,"is debited from your account.")
#         break
#     else:
#         print("account type doesnot match")
#         count = count + 1
# else:
#     print("invalid pin")
#     count =count +1
# if count ==3:
#     print("max tries exceeded,account blocked for 24 hours")
#     break

# TASK2 = making the user for 3 times.

# Index task solution:

# main_str = input("enter your main string:")

# substring = input("enter your main string:")

# if substring in main_str:
#     occurance=int(input("enter which occurance index:"))
    
# else:
#     print("substring not present in main string")


