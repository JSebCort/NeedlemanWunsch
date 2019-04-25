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





def brutForce(s1, s2):#checks all the passible options to find the best score 
    max = 0
    tmp = 0
    match = 1
    gap = -2 # scoring for strings 
    mismatch = -1
    score = 0
    temp1 = s1
    temp2 = s2
    best1 = ""
    best2 = ""
    check = 0
    

    if(s1 == s2):#inf thy are the same 
        print(s1)
        print(s2)
        print("score: " + len(s1))

    elif(len(s1) == len(s2)):#if they are the same length

        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                tmp = score
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i]):# checks for gaps
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):# checks for mismatch 
                        score += mismatch*j
                        i += j
                        break
                if(tmp == score):
                    score = mismatch*(len(s1)-i)
        
        max = score
        score = 0 # keeps track of highest score for comapred strings 
        best1 = s1
        best2 = s2
        s1 = temp1
        s2 = temp2

        for i in range(len(s1)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                tmp = score
                for j in range ((len(s1)-i)-1):

                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i+j]):
                        score += mismatch*j
                        i += j
                        break
                if(tmp == score):
                    score = mismatch*(len(s1)-i)

        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

        for i in range(len(s1)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                tmp = score
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

                   
                if(tmp == score):
                    score = mismatch*(len(s1)-i)
        
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2
                   
        for i in range(len(s1)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                tmp = score
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
                if(tmp == score):
                    score = mismatch*(len(s1)-i)
        
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2


    elif(len(s1) > len(s2)):# runs similar loops to check all possible combinations 

        for i in range(len(s2)-1):
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                for j in range ((len(s2)-i)-1):
                    
                    if(s1[i+j]==s2[i]):
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
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0 
        s1 = temp1
        s2 = temp2

        for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i+j]==s2[i]):
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
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

        for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
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

                    

        score += (len(s1)-len(s2))*gap
        if(score > max ):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2
                   
        for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
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

        score += (len(s1)-len(s2))*gap
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

                    

    else: #if the strings are not the same length

          for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                for j in range ((len(s2)-i)-1):

                   
                    if(s1[i+j]==s2[i]):
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
          if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2

          for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
            else:
                for j in range ((len(s2)-i)-1):

                    if(s1[i+j]==s2[i]):
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
          if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2

          for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
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

                   
          score += (len(s2)-len(s1))*gap
          if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2
                   
          for i in range(len(s2)-1):# runs similar loops to check all possible combinations 
            if(s1[i]==s2[i]):
                score += match
                check = check + 1
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
          score += (len(s1)-len(s2))*gap
          if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2


   if( check == 0):

            score = (len(s1))*-1
            print(score)
            print(s1)
            print(s2)

   else:
            score = max
            print(score)
            s2 = temp2
            print(best1)
            print(best2)
                   
    print("brutforce")
    print(best1)
    print(best2)
    print("Score: " , max)
    return(best2, score)


brutForce(list1,list2)