# CS 303E Exam 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

import math
from math import sqrt
# Problem 1: Pentagonal Procession
def pentagonalProcession():
    # replace pass with your solution to problem 1 here
    number=eval(input())
    n=1
    print(n,end="")
    while(n<number):
        n+=1
        pen=(3*n**2-n)/2
        print("",format(pen,".0f"),end="")
    
    pass

# Problem 2: Stellar Series
def stellarSeries():
    # replace pass with your solution to problem 2 here
    k=eval(input())
    n=0
    x=0
    while(n<k):
        n+=1
        x=x+sqrt(n)*2**(n-5)
    print(format(x,".2f"))
    pass

# Problem 3: Astonishing Average
def astonishingAverage():
    # replace pass with your solution to problem 3 here
    d=eval(input())
    n=1
    c=0
    p=1
    while(n<=50):
        if(n%d==0):
            p=p*n
            c+=1
        n+=1
    if(c==0):
        print("0.0")
    else:
        print(format(p/c,".1f"))


    pass

# Problem 4: The Wienni Waltz
def wienniWaltz():
    # replace pass with your solution to problem 4 here
    I=eval(input())
    a=eval(input())
    n=0
    print(format(a,".0f"),end="")
    while(n<4):
        if(a>I):
            a=a//3
            print("",format(a,".0f"),end="")
        elif(a<I):
            a=3*(a+8)
            print("",format(a,".0f"),end="")
        else:
            a=17*a-21
            print("",format(a,".0f"),end="")
        n+=1
    pass

# Problem 5: Coin Confusion
def coinConfusion():
    # replace pass with your solution to problem 5 here
    c=eval(input())
    n=0
    while(c>0):
        if (c-72>=0):
            c=c-72
            n+=1
        elif(c-24>=0):
            c=c-24
            n+=1
        elif(c-4>=0):
            c=c-4
            n+=1
        elif(c-1>=0):
            c=c-1
            n+=1
    print(format(n,".0f"))
    pass

# Problem 6: Letter Statistics
def letterLearning():
    # replace pass with your solution to problem 6 here
    character=input()
    if(65<=ord(character)<=90):
        print("uppercase")
        print(ord(character)-64)
    elif(97<=ord(character)<=122):
        print("lowercase")
        print(ord(character)-96)
    
    pass

# Problem 7: Greeting Generator
def greetingGenerator():
    time=eval(input())
    min=eval(input())
    shangxiawu=input()
    if(shangxiawu=="pm"):
        time=time+12
    if(time==24 and shangxiawu=="pm"):
        time=12
    if(time==12 and shangxiawu=="am"):
        time=0
    if(8<=time<=11):
        print("Good morning!")
    if(time==7):
        if(min>=30):
            print("Good morning!")
        else:
            print("You should be sleeping!")
    if(12<=time<=17):
        print("Good afternoon!")
    if(18<=time<=23):
        print("Good evening!")
    if(0<=time<=6):
        print("You should be sleeping!")
    # replace pass with your solution to problem 7 here
    pass

# Problem 8: Oscillating Operators
def oscillatingOperators():
    # replace pass with your solution to problem 8 here
    x=eval(input())
    y=eval(input())
    if(x**y<=10000):
        print(format(x**y,".2f"))
    else:
        print(format(x/y,".2f"))
    pass

if __name__ == "__main__":
    '''
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    '''
    # pentagonalProcession()
    # stellarSeries()
    # astonishingAverage()
    # wienniWaltz()
    # coinConfusion()
    # letterLearning()
    # greetingGenerator()
    # oscillatingOperators()
    pass