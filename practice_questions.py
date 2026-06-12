#ch-1
# #pratice question 1_addition of 2 input numbers
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
print("sum =",a+b)

#2_squaring
a=float(input("side of a square is"))
print("area of a square is",a*a)

#3_avg
a=float(input("1st floating number :"))
b=float(input("2nd floating number :"))
print("the average of floating point numbers is",(a+b)/2)

#4_>=?
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
print(a>=b)

#ch-2 
#5 WAP to input user’s first name & print its length.
str=input("enter the user's first name:")
print("length of the user's first name is :",len(str))

#6 WAP to find the occurrence of ‘$’ in a String.
str = "I have 2$ not 3$."
print(str.count("$"))

#7 WAP to input and grade students based on marks.
# marks >= 90, grade = A
# 90 > marks >= 80, grade = B
# 80 > marks >= 70, grade = C
# 70 > marks, grade = D

marks =int(input("marks of student :"))
if(marks>=90):
    print("grade=A")
elif(marks<90 and marks>=80): #reminder - and is a logical operator which gives true only when both left and right conditions are true.
    print("grade=B")
elif(marks<80 and marks>=70):
    print("grade=C")
else:
    print("grade=D")

#8 WAP to check if a number entered by the user is odd or even.
num = 7
if(num%2!=0):
    print("num is odd")
if(num%2==0):
    print("num is even")

#or

if(num%2!=0):
    print("num is odd")
else:
    print("num is even")

#9 WAP to find the greatest of 3 numbers entered by the user.
#approach 1

a=4
b=8
c=5
if(a>=b):
    if(a>=c): #nesting
        print("the greatest number is a:",a)
    else:
        print("the greatest number is c:",c)
elif(b>=c):
    print("the greatest number is b:",b)
else:
    print("the greatest number is c:",c)

#approach 2
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))
if(a>=b and a>=c): #logical operator : gives true as output only when left and right both conditions are true
    print("the greatest number is a :",a)
elif(b>=c):
    print("the greatest number is b :",b)
else:
    print("the greatest number is c :",c)

#10 WAP to check if a number is a multiple of 7 or not.

num=int(input("enter the number :"))
if(num%7==0):
    print("num is a multiple of 7")
else:
    print("num is not a multiple of 7")

#or

num=int(input("enter the number :"))
if(num%7==0):
    print("num is a multiple of 7")
if(num%7!=0):
    print("num is not a multiple of 7")


