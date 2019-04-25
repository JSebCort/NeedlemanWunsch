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

def Greedy(s1, s2, match , mispatch, gap):#finds the fastest soluion 
    max = 0
    tmp = 0
    match = 1 # scoring for difference in strings
    gap = -2
    mismatch = -1
    score = 0
    temp1 = s1
    temp2 = s2
    best1 = ""
    best2 = ""
    check = 0 

    if(s1 == s2):#if  strings are exactly the same 
        print(s1)
        print(s2)
        print("score" + len(s1))

    elif(len(s1) == len(s2)):#if theyre the same length loops throught 
        for i in range(len(s1)):
            if(s1[i]==s2[i]):# if characters match add 1 to match 
                score += match
                check = check + 1
            else:# if they dont match check what else is there
                tmp = score
                for j in range ((len(s1)-i)):

                    if(s1[i+j]==s2[i+j]):#misMatches 
                        score += mismatch*j

                        i += j
                        break

                if(tmp == score):#end cases 
                    score = mismatch*(len(s1)-i)
                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                      max = score
                      best1 = s1
                      best2 = s2
                score = tmp
                s1 = temp1
                s2 = temp2
                
                for j in range ((len(s1)-i)):
                    if(s1[i]==s2[i+j]):# checks for gaps
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                      max = score
                      best1 = s1
                      best2 = s2
                score = tmp
                s1 = temp1
                s2 = temp2


                for j in range ((len(s1)-i)-1):
                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                     max = score
                     best1 = s1
                     best2 = s2
                score = tmp
                s1 = temp1
                s2 = temp2
    else:
        if(s1 < s2):
            for i in range(len(s1)):
                if(s1[i]==s2[i]):# if characters match add 1 to match 
                    score += match
                    check = check + 1
                else:# if they dont match check what else is there
                    tmp = score
                    for j in range ((len(s1)-i)):

                        if(s1[i+j]==s2[i+j]):#misMatches 
                            score += mismatch*j

                            i += j
                            break

            if(tmp == score):#end cases 
                score = mismatch*(len(s1)-i)
            print(score)
            if(max < score):# keeps track of highest score for comapred strings 
                    max = score
                    best1 = s1
                    best2 = s2
            score = tmp
            s1 = temp1
            s2 = temp2
                
            for j in range ((len(s1)-i)):
                 if(s1[i]==s2[i+j]):# checks for gaps
                     score += gap*j
                     for k in range (j):
                         s1 = s1[:i+k] + '-' + s1[i+k:]
                     i += j
                     break

            print(score)
            if(max < score):# keeps track of highest score for comapred strings 
                max = score
                best1 = s1
                best2 = s2
            score = tmp
            s1 = temp1
            s2 = temp2


            for j in range ((len(s1)-i)-1):
                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

            print(score)
            if(max < score):# keeps track of highest score for comapred strings 
                     max = score
                     best1 = s1
                     best2 = s2
            score = tmp
            s1 = temp1
            s2 = temp2


        else:
                for i in range(len(s2)):
                    if(s1[i]==s2[i]):# if characters match add 1 to match 
                          score += match
                          check = check + 1
                    else:# if they dont match check what else is there
                        tmp = score
                        for j in range ((len(s2)-i)):

                            if(s1[i+j]==s2[i+j]):#misMatches 
                                score += mismatch*j

                                i += j
                                break

                if(tmp == score):#end cases 
                    score = mismatch*(len(s2)-i)
                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                      max = score
                      best1 = s1
                      best2 = s2
                score = tmp
                s1 = temp1
                s2 = temp2
                
                for j in range ((len(s2)-i)):
                    if(s1[i]==s2[i+j]):# checks for gaps
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                      max = score
                      best1 = s1
                      best2 = s2
                score = tmp
                s1 = temp1
                s2 = temp2


                for j in range ((len(s1)-i)-1):
                    if(s1[i+j]==s2[i]):
                        score += gap*j
                        for k in range (j):
                            s2 = s2[:i+k] + '-' + s2[i+k:]
                        i += j
                        break

                print(score)
                if(max < score):# keeps track of highest score for comapred strings 
                     max = score
                     best1 = s1
                     best2 = s2
                score = tmp
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

    print("Greedy")
    print(best1)
    print(best2)
    print("Score: " , max)    
    
    return(best2 , score)
                

Greedy(list1,list2)