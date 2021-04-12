# File: Student.py
# Student: zihao hong
# UT EID:zh4473
# Course Name: CS303E
# 
# Date Created:3/27
# Date Last Modified: 3/27
# Description of Program: object student thats waiting for you to enter 2 exam grades
class Student:
    def __init__(self, name,grade1="None",grade2="None"):
        self.exam1=grade1
        self.exam2=grade2
        self.name=name
    def __str__(self):
        if (self.exam1=="None"):
            exam1='None'
        else:
            exam1=format(self.exam1,".0f")
        if (self.exam2=="None"):
            exam2='None'
        else:
            exam2=format(self.exam2,".0f")
        return 'Student: '+self.name+'\n  Exam1: '+str(exam1)+'\n  Exam2: '+str(exam2)
    def getName(self):
        return self.name
    def getExam1Grade(self):
        if(self.exam1!="None"):
            return format(self.exam1,".0f")
    def getExam2Grade(self):
        if(self.exam2!="None"):
            return format(self.exam2,".0f")
    def setExam1Grade(self,grade):
        self.exam1=grade
    def setExam2Grade(self,grade):
        self.exam2=grade
    def getAverage(self):
        if(self.exam1=="None" or self.exam2=="None"):
            return 'Some exam grades not available.'
        else:
            return format((self.exam1+self.exam2)/2,".1f")