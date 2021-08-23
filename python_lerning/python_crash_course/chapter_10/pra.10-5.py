# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
filename = 'reasons.txt'
while True:
    reason = input("Why you like programming?")
    if reason == 'quit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(reason+'\n')