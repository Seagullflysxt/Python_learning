# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.22
"""
'''filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print("Hii")'''

filename = 'pi_million_digits.txt'

with open(filename) as file_project:
    lines = file_project.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
print("hi")
while True:
    birthday = input("Enter your birthday,in the form mmddyy:")
    if birthday == 'quit':
        break
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!\n")
    else:
        print("Your birthday does not appears in the first million digits of pi!\n")