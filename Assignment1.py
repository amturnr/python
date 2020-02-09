# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:55:06 2020

@author: amtur
"""

# Part 1 Creating Python Lists:

# a) print 1, 20 consecutively
a=[]
for i in range(1,21):
    a.append(i)
print(a)



# b) print 20,1 consecutively
b=[]
for i in range(1,21):
    b.insert(0,i)
print(b)

#c print 1:20:1
c=[a,b]

#d repeat [4,6,3] ten times

d=10*[4,6,3]

#e , similar to d but the last repetion should exclude 6,3
e = list.copy(d)
del e[-2]
print(e)

# Part 2: Create a list of the values of e^x cos(x) for x=3,3.1,...,6
import numpy
import math
myrange=numpy.arange (3,6.1,.1)
two=[]

# I initially tried to define the range in range but couldnt due to them not being integers
# I defined the range using arange instead
for i in myrange:
    two.append(math.exp(i) * math.cos(i))

# Part 3 create a list of the values 2, 2^2/2, 2^3/3,...,2^25/25
three=[]

for i in range(1,26):
    three.append(math.pow(2,i)/i)
    
# Part 4 - reusing the list from 1a create:


# [a0-an,a1-an-1,...,an-a0]
four_a=[]
for i in range(len(a)):
    four_a.append(a[i]-a[-i])

# true/false for even/odd

for i in range(len(a)):
    if a[i]%2 == 0:
        print(True)
    else:
        print(False)
        
# Part 5 - read lorem.txt

