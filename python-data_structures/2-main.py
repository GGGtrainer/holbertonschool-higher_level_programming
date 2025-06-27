#!/usr/bin/python3
replaceInList = __import__('2-replace_in_list').replaceInList

myList = [1, 2, 3, 4, 5]
idx = 3
newElement = 9
newList = replaceInList(myList, idx, newElement)

print(newList)
print(myList)