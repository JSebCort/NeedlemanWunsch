import re
import collections
import csv
import sys 
import random
from string import *



#s1 = input('Enter a file name: ')
list1 = "AAAAAAAAAAAAAAAAAAAAAAAAA"
#s2 = input('Enter a file name: ')
list2 = "GGGGGGGGGGGGGGGGGGGGGGGGG"

#list1 = "ACGTCAGGG"
#list2 = "ACGTCAGGC"


def Random(s1, s2, match, mismatch, gap):    

    min = 0
    tmp = 0
    #match = 1
    #gap = -2
    #mismatch = -1
    score = 0
    check = 0
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
        for i in range( len(temp1)-1 and len(temp2)-1):
            if( i < num ):
                print("")

            elif(temp1[i] == temp2[i]):
                  score = score + match
                  check = check + 1

            else:
                num = random.randint(0, 2)
                if(num == 0):
                    for j in range(len(temp1)-i-1 and len(temp2)-i-1):
                        

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
                     for j in range(len(temp1)-i-1 and len(temp2)-i-1):

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
                     for j in range(len(temp1)-i-1 and len(temp2)-i-1 ):
                         
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

        if( check == 0):

            score = (len(s1))*-1
            print(score)
            print(s1)
            print(s2)

        else:

            print(score)
            s2 = temp2
            print(s1)
            print(s2)

    return(s2, score)