# File: MyStringFunctions.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:4/2/2021
# Date Last Modified: 4/2/2021
# Description of Program: some sequence functions.
def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    x=0
    count=0
    while(x<len(str)):
        if(str[x]==ch):
            count+=1
        x+=1
    return count
def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    x=0
    newstring=str1
    while(x<len(str2)):
        newstring=newstring+str2[x]
        x+=1
    return newstring
def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    x=0
    if(len(str)==0):
        print("Empty string: no min value")
        return None
    else:
        ascii=ord(str[0])
        while(x<len(str)):
            if(ascii>ord(str[x])):
                ascii=ord(str[x])
            x+=1
        return chr(ascii)

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if(len(str)<i):
        print("Invalid index")
    elif(len(str)<1):
        return None
    elif(len(str)==i):
        return str[0:i+1]+ch
    else:
        return str[0:i]+ch+str[i:len(str)+1]
def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if(len(str)<=i):
        print("Invalid index",end='')
        return str,None
    else:
        return str[0:i]+str[i+1:len(str)+1],str[i]
def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    x=-1
    while(x<len(str)-1):
        x+=1
        if(str[x]==ch):
            return x
            break
    return -1
def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    x=len(str)-1
    while(x>=0):
        if(str[x]==ch):
            break
        x-=1
    return x
def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    x=0
    while(x<len(str)):
        if(str[x]==ch):
            break
        x+=1
    if(x==-1):
        return str
    return str[0:x]+str[x+1:len(str)+1]
def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    x=0
    newstring=''
    while(x<len(str)):
        if(str[x]!=ch):
            newstring=newstring+str[x]
        x+=1
    return newstring
def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order. 
    x=len(str)-1
    newstring=''
    while(x>=0):
        newstring=newstring+str[x]
        x-=1
    return newstring