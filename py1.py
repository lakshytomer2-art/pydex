"""#airthmetic operators
a = 12
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder modulus
print(a**b)#a^b

#relational operators
a=50
b=80

print(a==b).          multi line comment
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#assignment operators
a=5
print(a)
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a %= 5
print(a) #remainder
a=2
a **= 5
print(a) #modulus

#logical operators
print(not False)
print(not True)
a=10
b=12
print(not (a<b))
print(not (a>b))
print((a<b) and (a>b))
print((a<b) or (a>b))
print((a!=b) and (a<b))
print((a==b) or (a>b))"""

#type conversion
a=12 #automatically it is considered as float
b=12.6
print(a+b)
#12.0+12.6=24.6

#if i do the same with string it will concatenate
a="12"
b="12.6"
print(a+b)
#it will concatenate the two strings and give 1212.6 as output

"""a= "12"
b= 12.6
print(a+b)
#it will give error because we cannot add string and float together"""

#type casting
a= int("12") #manually converting string to integer
b= 12.6
print(type(a))
print(a+b) #automatically from integer to float

a= float("12") #manually converting string to float
b= 12.6
print(type(a))
print(a+b) 

a= str(12) #manually converting integer to string
b= "12.6"
print(type(a))
print(a+b) 

a=str(12.6) #manually converting float to string
b= "12.6"
print(type(a))
print(a+b)

a=1.2435
a=str(1.2435)
print(type(a))