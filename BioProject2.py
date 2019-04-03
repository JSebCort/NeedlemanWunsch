import re
import collections
import csv
import sys 
#import numpy as np
#from string import *



#s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACATGCA"
#s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATGCA"

    

def brutForce(s1, s2):
    min = 0
    match = 4
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
        print("score: 0 ")

    elif(len(s1) == len(s2)):

        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break
        
        min = score
        score = 0 
        best1 = s1
        best2 = s2
        s1 = temp1
        s2 = temp2

        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break
        
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break
        
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2
                   
        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break    
                    
                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break
        
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2


    elif(len(s1) > len(s2)):

        for i in range(len(s2)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break

        score += (len(s1)-len(s2))*gap
        min = score
        score = 0 
        best1 = s1
        best2 = s2
        s1 = temp1
        s2 = temp2

        for i in range(len(s2)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break

        score += (len(s1)-len(s2))*gap
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

        for i in range(len(s2)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

        score += (len(s1)-len(s2))*gap
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2
                   
        for i in range(len(s2)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break    
                    
                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

        score += (len(s1)-len(s2))*gap
        if(score < min):
            min = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

                    

    else:

          for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break
          score += (len(s2)-len(s1))*gap
          min = score
          score = 0 
          best1 = s1
          best2 = s2
          s1 = temp1
          s2 = temp2

          for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break
          score += (len(s2)-len(s1))*gap
          if(score < min):
            min = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2

          for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break
          score += (len(s2)-len(s1))*gap
          if(score < min):
            min = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2
                   
          for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break 

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break    
                    
                    elif(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 =  s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break
          score += (len(s1)-len(s2))*gap
          if(score < min):
            min = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2

                   

    print(best1)
    print(best2)
    print("Score: " , min)


brutForce(list1,list2)



