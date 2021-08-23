# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'guest.txt'

name = input("Enter your nane:")
with open(filename,'w') as file_object:
    file_object.write(name+'\n')