#!/usr/bin/python3
jump = (101, 113)
for letter in range(97, 123):
    if letter in jump:
        continue
    print("{:c}".format(letter), end='')
    