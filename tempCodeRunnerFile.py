list=[2,1,2]
copied_list=print(list.copy())
list.reverse()
print(list)
if(copied_list==list):
    print("list contains a palindrome of elements")
else:
    print("not a palindrome")