# CS 303E Mock Exam (homework 6)
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Sphere Surface Area
import math
def sphereSurfaceArea():
    # write your solution to problem 1 here
    r=eval(input())
    if(r<0):
        print("Negative radius entered ")
    else:
        area=4*math.pi*r**2
        print(format(area,".2f"))
    pass



# Problem 2: Make Uppercase
def makeUppercase():
    # write your solution to problem 2 here
    character=input()
    diff=ord('a')-ord('A')
    if(97<=ord(character)<=122):
        print(chr(ord(character)-diff))
    else:
        print(character)
    pass



# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    n=eval(input())
    if (n>=2):
        sum=0
        while(n>=2):
            a=(n-1)*n
            sum=sum+a
            n=n-1
        print(sum)
    else:
        print("error")
    pass



# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    a=eval(input())
    b=eval(input())
    c=eval(input())
    if(b>=a and b>=c):
        max=b
    elif(c>=a and c>=b):
        max=c
    else:
        max=a
    if(b<=a and b<=c):
        min=b
    elif(c<=a and c<=b):
        min=c
    else:
        min=a
    if(a!=max and a!=min):
        mid=a
    elif(b!=max and b!=min):
        mid=b
    else:
        mid=c
    print(min,mid,max)
    pass



# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    num=float(input())
    if (num==0):
        FloatSum=num
    else:
        FloatSum=num
        if(FloatSum<0):
            FloatSum=0
        while(num!=0):
            num=float(input())
            if(num>0):
                FloatSum+=num
    print(format(FloatSum,".3f"))
    pass



# Problem 6: Print Squared Table
def printSquaredTable():
    # write your solution to problem 6 here
    num=eval(input())
    n=0
    print("  n      n**2\n-------------")
    while (n<num):
        n+=1
        print(format(n,"3"),format(n**2,"10"),sep="")
    pass



# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    num=eval(input())
    x=1
    while(x**2<=num):
        x+=1
    print(x-1)
    pass



# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    num=eval(input())
    n=1
    while(num!=1):
        if(num%2==0):
            num=num/2
            n+=1
        else:
            num=3*num+1
            n+=1
    print(n)
    pass


