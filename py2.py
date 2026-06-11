#chapter 2

str1="hello"
str2='myself lakshy'
str3='''age:20'''

try:
    # Python will try to read this, but it will fail syntax checking
    exec("'THIS IS MY FRIEND'S TUTORIAL'") 
except SyntaxError:
    print("Line 9 gives a SyntaxError because the apostrophe closes the single quote early and python won't be able to interpret the remaining data")

#it won't work das why we need "",'',''''''.
#correct way
"this is my friend's tutorial"
'this is my friend"s tutorial'

#escape sequence characters
str1="my name is lakshy tomer.\ni am 20 years old"
print(str1) #\n is used for skipping lines
str1="my name is lakshy tomer.\ti am 20 years old"
print(str1) #\t is used for tab space"""

#basic operations

#concatenation
str1 = "lakshy"
str2 = "tomer"
final_string = str1+str2
print(final_string)

#length of a str
print(len(str1))
print(len(str2))
#or
len1 = len(str1) 
len2 = len(str2)
print(len1)
print(len2)
print(len(final_string))

str1 = "lakshy  "
print(len(str1))  #len count spaces,special symbols and characters too. 

#indexing
str1 = "lakshy tomer"
print(str1[0])
print(str1[2])
print(str1[6])
print(str1[11])

#with the help of index we can only access the characters but can't manipulate/modify them.

#slicing 
str1 = "eren ken" #Accessing parts of a string
print(str1[0:4])  #str[ starting_idx : ending_idx ] #ending idx is not included
print(str1[5:8])

#or
print(str1[5:len(str1)])

#or
print(str1[5:]) #[5:len(str1)]
print(str1[:4]) #[0:4]"""

#negative slicing

str = "apple"
print(str[-5:-3]) #ending idx is not included
print(str[-3:-1])

#string functions
str = "hello world"
print(str.endswith("ld")) #returns true if string ends with substr
print(str.capitalize())   #capitalizes 1st char
