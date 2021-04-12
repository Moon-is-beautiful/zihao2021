# File: Payroll.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:2/12/2021
# Date Last Modified: 2/12/2021
# Description of Program: read inputs of pay rate and tax rate then reture net pay and details about deduction

import math
a=input("Enter employee's name: ")
b=float(input("Enter number of hours worked in a week: "))
c=float(input("Enter hourly pay rate: "))
d=float(input("Enter federal tax withholding rate: "))
e=float(input("Enter state tax withholding rate: "))
fed_rate_percent=round(d*100,1)
state_rate_percent=round(e*100,1)
f=b*c
g=f*d
h=f*e
i=g+h
j=f-i
print("\nEmployee Name: ",a,"\nHours Worked: ",b,"\nPay Rate: $",c,"\nGross Pay: $",format(f,".2f"),"\nDeductions:\n  Federal Withholding (",fed_rate_percent,"%): $",format(g,".2f"),"\n  State Withholding (",state_rate_percent,"%): $",format(h,".2f"),sep="")
print("  Total Deduction: $",format(i,".2f"),"\nNet Pay: $",format(j,".2f"),sep="")
