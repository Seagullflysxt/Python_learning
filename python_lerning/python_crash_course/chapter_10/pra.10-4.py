# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'guest_book.txt'

while True:
    name = input("Enter your name:")
    if name == 'quit':
        break
    print(f"Hello,{name}")
    with open(filename,'a') as file_object:
        file_object.write(f"{name} visited.\n")