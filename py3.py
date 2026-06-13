#ch-3

#lists
marks1=44.5
marks2=44.9
marks3=66.5 #not efficient
marks4=12.9
marks5=98.2

#or

marks=[44.5,44.9,66.5,12.9,98.2]
print(marks)        #efficient
print(type(marks))  #<class 'list'>
print(marks[0])
print(marks[4])     #idx
print(len(marks)) 

#It can store elements of different types (integer, float, string, etc.)
#C++ Array: It is strictly homogeneous.
#Python List: It is completely heterogeneous.

std = ["kartavya",25,"delhi"]
#combination of strings and int
print(std)
print(std[1])
print(std[2])
print(len(std))
