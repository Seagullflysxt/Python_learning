# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'learning_python.txt'

with open(filename) as file_project:
    for line in file_project:
        print(line.replace('Python','C'))