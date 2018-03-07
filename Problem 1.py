# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:45:25 2018

@author: Muhammad Amin


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

ub = int(input("Enter the upper bound "))

mult_three = []
mult_five =[]

for i in range(ub):
    if i % 3 == 0:
        mult_three.append(i)
    elif i % 5 ==0:
        mult_five.append(i)

total = sum(mult_three) + sum(mult_five)
print (total)

