def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    x=len(str)-1
    while(x>=0):
        if(str[x]==ch):
            break
        x-=1
    return x