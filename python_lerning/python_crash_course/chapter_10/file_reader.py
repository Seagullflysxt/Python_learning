# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.22
"""
'''with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())'''

filename = 'pi_digits.txt'

'''with open(filename) as file_project:
    for line in file_project:
        print(line.rstrip())
print("Hello!")'''

with open(filename) as file_project:
    lines = file_project.readlines()

for line in lines:
    print(line.rstrip())

print("Hello!")
