# File: MinMax.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:3/5/2021
# Date Last Modified:3/5/2021 
# Description of Program:keeps asking you for numbers till you type stop
# and when you type in stop it gives you the maximum and the minimum number you entered.

import math
first=(input("Enter an integer or 'stop' to end: "))
if (first=="stop"):
    print("You didn't enter any numbers")
else:
    max=min=num=eval(first)
    while(True):
        num=input("Enter an integer or 'stop' to end: ")
        if(num=="stop"):
            break
        else:
            num=eval(num)
            if(num>=max):max=num 
            if(num<=min):min=num 
    print("The maximum is",max)
    print("The minimum is",min)
