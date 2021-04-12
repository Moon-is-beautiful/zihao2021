# File: DaysInMonth.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created: 2/25/2021
# Date Last Modified: 2/25/2021
# Description of Program: tells you how many days a month has.
import math
y=int(input("enter the year: "))
m=int(input("enter the month: "))
if (y%4==0):
    if(y%100==0):
        if(y%400==0):
            IsLeapYear=True
        else:
            IsLeapYear=False
    else:
        IsLeapYear=True
else:
    IsLeapYear=False

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    n=31
else:
    if(m==2):
        if(IsLeapYear==True):
            n=29
        else:
            n=28
    else:
        n=30
if (m==1):
    w="January"
if (m==2):
    w="February"
if (m==3):
    w="March"
if (m==4):
    w="April"
if (m==5):
    w="May"
if (m==6):
    w="June"
if (m==7):
    w="July"
if (m==8):
    w="August"
if (m==9):
    w="September"
if (m==10):
    w="October"
if (m==11):
    w="November"
if (m==12):
    w="December"
print(w,y,"has",n,"days")