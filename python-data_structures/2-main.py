#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

myList = [1, 2, 3, 4, 5]
idx = 3
newElement = 9
newList = replace_in_list(myList, idx, newElement)

print(newList)
print(myList)