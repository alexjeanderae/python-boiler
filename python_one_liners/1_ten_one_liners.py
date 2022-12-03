
# 1 Swap two variables

a = 4 
b = 5
print(a,b)
a,b = b,a # the one liner
print("they are now swapped " + str(a) +" "+ str(b))
# >> 5,4

# 2 Multiple Variable Assignments with same or DIFFERENT type
a,b,c = 4,5.5,'Hello' # the one liner with a int, a float and a str
print(type(a),type(b),type(c))
# >> <class 'int'> <class 'float'> <class 'str'>
print(a,b,c)
# >> 4 5.5 Hello

# 3 Multiple Variable Assignments with same or DIFFERENT type AND a list for the last part
a,b,*c = [1,2,3,4,5] # the one liner with c the last variable preceded with *
print(a,b,c) 
# >> 1 2 [3, 4, 5]

# 4 Sum of even numbers in a list
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0]) # the one liner
print(s)
# >> 12

# 5 Deleting Multiple Elements from a List with the del keyword

## extended slices aa[start:end:step] and is all on the index, python does not look at the content here

#### Deleting all the even numbers
a = [1,2,3,4,5]
del a[1::2] # the one liner
print(a)
# >>[1, 3, 5]
# this one uses the "extended slices", jumping by 2 starting at index 1

#### Deleting all the numbers at odd index
a = [1,2,3,4,5]
del a[::2] # the one liner, no need to write index 0 as starting
print(a)
# >>[2, 4]
# this one uses the "extended slices", jumping by 2 starting at index 0

#### Deleting fourth and everything after (start at index 3 till the end)
a = [1,2,3,4,5]
del a[3::] # the one liner
print(a)
# >>[1, 2, 3]

#### Deleting third and fourth (start at index 2, take third and finish at index 4)
a = [1,2,3,4,5]
del a[2:4:] # the one liner
print(a)
# >>[1, 2, 5]

# 6 reading a (txt) file line by line

##Using the keyword "with" will also close the file after use
with open("data.txt") as f: lst=[line.strip() for line in f] # the one liner with strip to remove unnecessary space
print(lst)
# FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
# check that your terminal is in the right folder!

# 7 write data to a (txt) file
with open("data.txt",'a',newline='\n') as f: f.write("Python is awesome")
# TODO: newline seems finicky. In my case it seems to collate to previous line

# 8 create a list using range
lst = list(range(0,10))
print(lst)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 9 add strings in a list of strings
lst = [("Hello "+i) for i in ['Karl','Abhay','Zen']]
print(lst)
# >> ['Hello Karl', 'Hello Abhay', 'Hello Zen']

# 10 change the type of a whole list using map instead of iteration (aka Typecasting)

##Example we have a few values we handpicked and they are currently strings and we want them float
lst = list(map(float,['1','34','270']))
print(lst)
# >> [1.0, 34.0, 270.0]