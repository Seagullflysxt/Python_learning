# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
import json

username = input("What's your name?")

filename = 'username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"We'll remember you when you came back,{username}!")