# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)