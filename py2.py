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
print(str1) #\t is used for tab space

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
print(str1[:4]) #[0:4]

#negative slicing

str = "apple"
print(str[-5:-3]) #ending idx is not included
print(str[-3:-1])

#string functions
str = "hello world"
print(str.endswith("ld")) #returns true if string ends with substr, str.endsWith(“")
print(str.capitalize())   #capitalizes 1st char, str.capitalize( )
print(str.replace("l","r"))
print(str.replace("hello","hi")) #replaces all occurrences of old with new, str.replace( old, new )
print(str.find("l"))
print(str.find("world")) #returns 1st index of 1st occurrence
print(str.count("l"))
print(str.count("world")) #counts the occurrence of substr in string 

#conditional statements
#if condition
age = 24
if(age>=18):
    print("can drive")

#elif condition (else if)   
traffic_light = "red"
if(traffic_light=="red"):
    print("stop")
if(traffic_light=="yellow"):
    print("wait")
if(traffic_light=="green"):
    print("go") 

#difference between if and elif conditions: if conditions are always evaluated independently. If you have five separate if statements in a row, Python will check every single one of them, one after the other and all the false if statements will be executed with an absolutely zero output.
#elif (else-if) conditions are linked to the if statement above them. They form a chain. Python only checks an elif if all the conditions above it in that chain were false.
#The moment Python finds a true condition inside an if-elif chain, it executes that specific block of code and skips (ignores) the entire rest of that chain below it.

#case-1
num = 5
if(num>2):
    print("num is greater than 2")
if(num>3):
    print("num is greater than 3")

#case-2
num = 5
if(num>2):
    print("num is greater than 2")
elif(num>3):
    print("num is greater than 3")

#else condition

#case-1
traffic_light = "pink"
if(traffic_light=="red"):
    print("stop")
elif(traffic_light=="yellow"):
    print("wait")
elif(traffic_light=="green"):
    print("go")
else:
    print("go back")
#case-2
age = 19
if(age<=18):
    print("cannot drive") #indentation: proper spacing after if,elif or else statements or before the print statement
else:
    print("can drive")
