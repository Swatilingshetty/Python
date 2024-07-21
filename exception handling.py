
# 23/04/24
# exception: Errors are nothing but exceptions..
# exception handling : handling the slow of errors..

# inbuilt exceptions:
                # those exceptions which comes directly with the respective programming language
# user defined exception:
                # those exceptions which user defines depending on the requirments..

# try and except

# try:
#     statements         # this should contains these lines which might give an error 
# except:
#     statements         # those lines which should be executed when an error occurence in try block..

list1=[12,14,23,"python",43,4,0,44]   # 0 is occured error not any value

# for ele in list1:
#     print(1/ele)

# import sys
# for ele in list1:
#     try:
#         print(1/ele)
#     except:
#         print(sys.exc_info()[0])
#         print("some error occured")



# for ele in list1:
#     try:
#         print(1/ele)
#     except TypeError:
#         print("passed different type of values for division")

#     except ZeroDivisionError:
#        print("dicision with zero is not possible")

list1=[12,14,23,"python",43,4,0,44]

for ele in list1:
    try:
        print(1/ele)
    except (TypeError,ZeroDivisionError):
        print("passed different type of values for division")
    else:
        print("no error occured")     # else will get executes only when there is not error