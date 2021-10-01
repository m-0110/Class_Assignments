'''
PROGRAM DESCRIPITON:
	Find the factorial of numbers in given range using numpy and store them in a JSON file.
    Also find the karperkar numbers in given range and store them in same JSON file.
'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None



import numpy as np
import json
dic={}

# find factorial from 1 to 100 and store  as {  1:factorial(1) ...} using  factorial  method in numpy
for i in range(1,101):
    dic[i]=np.math.factorial(i)

#storing factorial from 1 to 100 as dictionary in dic1
dic1={"factorial":dic}

#used to find number of  digits in square of number in finding kaprekar number
def count_digits(n):
    count=0
    while(n>0):
        n=n/10
        count+=1
    return count

#check number is kaprekar number or not
def kaprekar_number(n):
    if(n==1):
        return True
    square=n*n
    count=count_digits(square)
    #print(square)
    for i in range(1,count):
        p=pow(10,i)
        if(p==n):
            return False
        #break into 2 parts
        part1=square//p
        part2=square%p
        #check sum is equal to given number
        if(part1+part2==n):
            return True

    return False
kaprekar=[]
for i in range(1,10001):
    if(kaprekar_number(i)):
        kaprekar.append(i)
#print(kaprekar)
#storing kaprekar numbers
dic2={"kaprekar_numbers":kaprekar}




#dumping into json file  dic1 has factorials and dic2 as kaprekar numbers
with open("day8.json","w") as file:
    json.dump([dic1,dic2],file)

