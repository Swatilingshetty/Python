# loops or iteration : executing certain code repeatedly

# while loop 
# for loop 

# while loop : its the infinite loop (it will run the statements continuously while the condition is false)

# while condition:
#     statements

a = 3

# while a<=10:
#      print(a)
#      a+=1
# print(a)

if a>=8:
   print(a)
#    a+=1
#    a+=2
#    a+=3
print(a)    



# for loop : its a loop which will execute the statements for certain number of lines 

# for element is sequences:
#     statements

# the way how the iterations are going to depends upon the value that considering
# for ele in "pythonprogramming":
#     print(ele)
#     print("hello")

# list1 = [1,'python','data',4,5,12,19,'devops']

# for ele in list1:
#     print(ele) 

# dict1 = {'name':'sai','age':23,'sal':25000,'company':'tcs'}

# for ele in dict1:
#     print(ele)

# range : it is the function which will generate the sequence of number..

for ele in range(1,25):
    print(ele)

for ele in range(25):
    print(ele)

for ele in range(1,11):
    # print("simple text"+str(ele))
    print("swati"+str(ele))

# for ele in range(1,31,4): (jump or offset)  #[1,5,9,13,17,21,15,29]
#     print(ele)

# for ele in range(1,15,1):  
#     print(ele)

# for ele in range(20,1,-1):
#     print(ele)

# str1 = "python is a programming language"

# indexing == accessing the elements in the sequence is done its indexing   (list,str,tuple)
# indexing will start from 0...
# we can use [] to access the indexing..

# print(str1[0])

# print(str1[15])

# print(str1[20])

# if 40 < len(str1):
#     print(str1[40])

# list1 = ['python',12,4,5,'django',54,8,6]

# print(list1[0])

# print(list1[6])

# print(str1[7:19])

# print(list1[2:7])

# for ele in str1[7:19]:
#     print(ele)

# print(str1[3:30 :3])

# positive indexing : performing the indexing from right to left.
# negative indexing : performing the indexing in reverse order.

# negative indexing will start from -1

# print(str1[-1])

# print(str1[-7])       

# print(str1[-2:-11:-1])

# print(list1[-5])

# print(list1[-7])

# print(list1[-3:-6:-2])

# when we want to perform indexing or range in reverse order, we have to make sure we specified the 3rd element as negative value only...

#control flow statements : controling the flow of iterations...

#Break == it will stop all the iteration and come out of the loop..
#Continue == it will skip the current iteration and will go to the next directly..

# for ele in range(1,50):
#     if ele%2==0 and ele%5==0:
#         print(ele)
#         break


# for ele in range(1,50):
#     if ele%3==0 and ele%5==0:
#         continue
#        # print(ele)
#     print(ele,"is not multiple of 3 and 5")
    

# for ele in range(1,30):
#     if ele%2==0 and ele%4==0:
#         continue
#         print(ele)
#     print(ele,"is multiple of 2 and 4 ")