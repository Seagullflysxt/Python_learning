# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasheets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")