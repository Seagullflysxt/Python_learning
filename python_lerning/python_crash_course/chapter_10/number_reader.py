# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)