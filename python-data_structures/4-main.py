#!/usr/bin/python3
newInList = __import__('4-new_in_list').newInList

myList = [1, 2, 3, 4, 5]
idx = 3
newElement = 9
newList = newInList(myList, idx, newElement)

print(newList)
print(myList)