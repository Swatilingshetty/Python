# Identify operators(is,is not): compare the memory location of two objects.

# a=34
# b=34
# print(id(a))
# print(id(b))

# print(a is b)

# name="ramesh"
# name1="ramesh"
# print(id(name))
# print(id(name1))

# print(name is name1)

# name="swati"
# name1="archana"
# print(id(name))
# print(id(name1))

# print(name is name1)

# tuple={1,2,3}
# tuple1={1,2,3}
# print(id(tuple))
# print(id(tuple1))

# print(tuple is tuple1)

# list = [1,2,3]
# list1 = [1,2,3]

# print(id(list))
# print(id(list1))

# print(list is list1)

# memory allocatoin  for mutable objects will be different for every object.object
# memory allocation for immutable objects will be  same for every object.object
    
#Bitwise operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Bitwise NOT(~),,Right shift(>>),left shift(<<)

# A      B     A&B     A|B       A^B
# -----------------------------------
# 0      1      0       1         1
# 1      0      0       1         1
# 1      1      1       1         0
# 0      0      0       0         0

# print(12 & 21)

# print(12 | 21)

# print(12 ^ 21)

# 12 - 01100
# 21 - 10101

# 01100 - 12
# 10101 - 21
# ----------
# 00100 - 
# 11101 - 
# 11001 - 

# print(int('100',2))
# print(int('11101',2))
# print(int('11001',2))

#Left shift : shift the bits to the left by the specified number of places, and assigns 0 to the shifted places

#print(21 << 1)

#21 - 00010101
#00101010 - 21<1

#print(int('101010',2))

#print(21>>2)

# Bitwise not(~): inverts all the bits of the number

# a = 10
# print(~a)

#10 - 0000 1010
#   - 1111 0101 -- 1's compliment -- 

#1's complement : 0000 1010
#                        +1
#--------------------------------
#                + 0000 1011 -- 2's complement

#print(int('-1011',2))

a=14
-(a+1)

print(~a)
b = -11
print(~b)  











                