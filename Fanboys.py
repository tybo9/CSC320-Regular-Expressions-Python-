#Ayoub Rammo
#CS320
#Regular Expressions

import re

#read data file
def readFile():
    f=open("data.txt",'r') #file name
    l=list(f.readlines()) #reading lines
    for i in range(len(l)):
        l[i]=l[i][:-1]
    return l

#identify fanboy
def doFanboys(mylist):
    string=mylist[0]
    string=re.sub(", for"," FANBOYS",string)
    string=re.sub(", yet"," FANBOYS",string)
    string=re.sub(", so"," FANBOYS",string)
    string=re.sub(", and"," FANBOYS",string)
    string=re.sub(", nor"," FANBOYS",string)
    string=re.sub(", but"," FANBOYS",string)
    string=re.sub(", or"," FANBOYS",string)
    count =  string.count("FANBOYS")
    return count,string

#call function
lines = readFile()

#get fanboys
count,string = doFanboys(lines)

#split them up into three
newList=string.split("FANBOYS")
newList = string.split(".")
for i in range(len(newList)):
    newList[i]=newList[i].strip()
    print(i+1,":", newList[i])
    print()

