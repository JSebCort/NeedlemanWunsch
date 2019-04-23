import re
import collections
import csv
import sys 
#import GUI as data
from string import *



#s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACATGCA"
#s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATGCA"

list1 = "ACGTCAGGG"
list2 = "ACGTCAGGC"

def DivideConquer(s1, s2):# devideds up strings and compares them
    max = 0
    tmp = 0
    match = 1
    gap = -2
    mismatch = -1
    score = 0
    temp1 = s1
    temp2 = s2
    best1 = ""
    best2 = ""

    if(s1 == s2):
        print(s1)
        print(s2)
        print("score" + len(s1))

    #elif():




DivideConquer(list1, list2)
