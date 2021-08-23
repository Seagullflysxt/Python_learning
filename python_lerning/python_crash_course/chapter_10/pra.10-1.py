# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'learning_python.txt'
#1
print("Method 1:")
with open(filename) as file_project:
    contents = file_project.read()
print(contents)

#2
print("Method 2:")
with open(filename) as file_project:
    for line in file_project:
        print(line.rstrip())
#3
print("Method 3:")
with open(filename) as file_project:
    lines = file_project.readlines()
print(lines)
for line in lines:
    print(line.rstrip())