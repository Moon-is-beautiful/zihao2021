# File: FindPrimeFactors.py
# Student: zihao    
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:4/9/2021
# Date Last Modified: 4/9/2021
# Description of Program: find prime factors
import math
def isPrime(num):
    if(num<2 or num % 2 ==0):
        return(num==2)
    divisor=3
    while(divisor<=math.sqrt(num)):
        if(num%divisor==0):
            return False
        else:
            divisor+=2
    return True
def findNextPrime(num):
    if(num<2):
        return 2
    if(num%2==0):
        num-=1
    guess=num+2
    while(not isPrime(guess)):
        guess+=2
    return guess
def findPrimeF(num):
    if(isPrime(num)):
        return list([num])
    else:
        factors=list()
        d=2
        while(num>1):
            if(num%d==0):
                factors.append(d)
                num=num/d
            else:
                d=findNextPrime(d)
        return factors
while(True):
    dababy=eval(input("Enter a positive integer (or 0 to stop): "))
    if(dababy== 0):
        print("Goodbye!")
        break
    elif(dababy<0):
        print("  Negative integer entered.  Try again.")
    elif(dababy==1):
        print("  1 has no prime factorization.")
    else:
        print("  The prime factorization of 104 is:",findPrimeF(dababy))
    