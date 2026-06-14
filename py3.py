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

# Strings are Immutable (Cannot be changed/manipulated).
# Lists are Mutable (Can be changed/manipulated).

std = ["kartavya",25,"delhi"]
std[0]="ashutosh"
print(std)  #mutable lists

str="hello"
print(str[0])
try:
    str[0]="g" #TypeError: 'str' object does not support item assignment
except TypeError:
    print("error:you cannot modify a string because strings are immutable!")

#list slicing
#list_name[ starting_idx : ending_idx ] #ending idx is not included
#similiar to string slicing

marks=[84,98,99,83,87]
print(marks[1:4])
print(marks[-3:-5]) #By default, Python slices from left to right
                    #Output: [] ❌ Empty List!
print(marks[-5:-3]) #negative slicing

#list methods
#like string functions

list=[2,3,5,6]   #To actually see your updated list, you have to separate the action line from the print line or it will print "None" on your screen unlike string functions.
list.append(0)   #adds one element at the end
print(list)   
list.sort()      #sorts in ascending order
print(list)
list.sort(reverse=True)  #sorts in descending order
print(list)
list.reverse()   #reverses list
print(list)
list.insert(3,9) #list.insert( idx, el ) #insert element at index
print(list)
list=[2,3,4,2]
list.remove(2)  #removes first occurrence of element
print(list)
list.pop(1)
print(list)     #removes element at idx

#tuple
#Lists are mutable (you can change them).
#Tuples (and strings) are immutable.

tuple=(2,3,6,7,1)
print(type(tuple))
print(tuple)
print(tuple[2]) #indexing brackets are ALWAYS square [].

tup=(1,) #correct way to represent single element tuple
print(type(tup))
print(tup)

tup=(1) #incorrect way to represent single element tuple
print(type(tup)) 
print(tup)

#tuple methods
#The Tuple Rule: CAN print on the same line
#The String Rule: CAN print on the same line
#The List Rule: IT DEPENDS!
      #The Changers (Do NOT print on the same line):append(), .extend(), .insert(), .remove(), .sort(), .reverse().
      #The Informers (CAN print on the same line):len(), .count(), .index().
      #Exception to the Rule: .pop():CAN print it on the same line
tup=(1,2,3,4,4,3,2,1)
print(tup.index(4)) #returns index of first occurrence
print(tup.count(4)) #counts total occurrences












