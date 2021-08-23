# -*- coding:utf-8 -*-
"""
作者：Seagull
日期：2021.07.23
"""
import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back,{username}!")