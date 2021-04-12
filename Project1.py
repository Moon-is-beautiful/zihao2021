# File: Project1.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:3/24/2021
# Date Last Modified: 3/24/2021
# Description of Program: generate grade report
name=input("\nEnter the student's name: ")
print("\nHOMEWORKS:")
def askforgrade(one,two,three):
    while(True):
        print("  Enter",one,"grade: ",end="")
        grade=eval(input())
        if(two<=grade<=three):
            break
        else:
            print("  Grade must be in range [", two, "..", three, "]. Try again.",sep="")
    return grade
HW1=askforgrade("HW1",0,10)
HW2=askforgrade("HW2",0,10)
HW3=askforgrade("HW3",0,10)
print("\nPROJECTS:")
Project1=askforgrade("Project1",0,100)
Project2=askforgrade("Project2",0,100)
print("\nEXAMS:")
Exam1=askforgrade("Exam1",0,100)
Exam2=askforgrade("Exam2",0,100)
print("\nGrade report for: Susie Student")
HWaverage=(HW1+HW2+HW3)/3*10
PROaverage=(Project1+Project2)/2
EXaverage=(Exam1+Exam2)/2
Overall=HWaverage*.3+PROaverage*.3+EXaverage*.4
if(90<=Overall<=100):
    letter="A"
elif(80<=Overall<90):
    letter="B"
elif(70<=Overall<80):
    letter="C"
elif(60<=Overall<70):
    letter="D"
elif(0<=Overall<60):
    letter="F"
print("  Homework average (30% of grade):",format(HWaverage,".2f"))
print("  Project average (30% of grade):",format(PROaverage,".2f"))
print("  Exam average (40% of grade):",format(EXaverage,".2f"))
print("  Student course average:",format(Overall,".2f"))
print("  Course grade (CS303E: Spring, 2021):",letter,"\n")