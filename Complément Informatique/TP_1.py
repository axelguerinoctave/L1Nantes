# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:53:01 2020

@author: Axel
"""
    

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(0))