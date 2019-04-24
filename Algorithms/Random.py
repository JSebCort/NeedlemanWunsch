import re
import collections
import csv
import sys 
import random
from string import *



#s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACAATGCA"
#s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATAAAGTCCGCTGCA"

#list1 = "ACGTCAGGG"
#list2 = "ACGTCAGGC"


def Random(s1, s2):    

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
    num = 0
    rand = 0
     

    if(s1 == s2):
        print(s1)
        print(s2)
        print("score" + len(s1))
        

    else:
        for i in range( len(temp1) and len(temp2)):
            if( i < num ):
                print("")

            elif(temp1[i] == temp2[i]):
                  score = score + match

            else:
                num = random.randint(0, 2)
                if(num == 0):
                    for j in range(len(temp1) and len(temp2) ):
                         if( temp1[j+i] == temp2[j+i]):
                            score = score + (mismatch*j)
                            num =j + i
                            break
                         elif( temp1[i] == temp2[j+i]):
                            score = score + (gap*j)
                            num = j + i
                            break
                         elif(temp1[j+i] == temp2[i]):
                            score = score + (gap*j)
                            num = j + i
                            break


                elif(num  == 1):
                     for j in range(len(temp1) and len(temp2)):

                         if( temp1[i] == temp2[j+i]):
                            score = score + (gap*j)
                            num = j + i
                            break

                         elif( temp1[j+i] == temp2[j+i]):
                            score = score + (mismatch*j)
                            num =j + i
                            break
                         
                         elif(temp1[j+i] == temp2[i]):
                            score = score + (gap*j)
                            num = j + i
                            break


                elif(num == 2):
                     for j in range(len(temp1) and len(temp2) ):
                         
                         if( temp1[i] == temp2[j+i]):
                            score = score + (gap*j)
                            num = j + i
                            break
                         elif(temp1[j+i] == temp2[i]):
                            score = score + (gap*j)
                            num = j + i
                            break
                         elif( temp1[j+i] == temp2[j+i]):
                            score = score + (mismatch*j)
                            num =j + i
                            break
        print(score)
        print(temp1)
        print(temp2)

Random(list1, list2)
