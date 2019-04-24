import re
import collections
import csv
import sys 
from string import *



#s1 = input('Enter a file name: ')
s1 = "ATGTAGTGTATAAAGTACATGCA"
#s2 = input('Enter a file name: ')
s2 = "ATGTAGTACATGCA"

#list1 = "ACGTCAGGG"
#list2 = "ACGTCAGGC"

def divide(string, devlength): 
    split = []
    split = split + list(string[0+i:devlength+i] for i in range(0, len(string), devlength))
    
    return split
    

def DivideConquer(s1, s2):# devideds up strings and compares them
    devlength = 10
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
    list1 = []
    list2 = []
    gap1 = 0
    gap2 = 0
    totalgap = 0
    endgap = 0
    num = 0
     

    if(s1 == s2):
        print(s1)
        print(s2)
        print("score" + len(s1))
        

    else:
        list1 = divide(s1, devlength)
        list2 = divide(s2, devlength)

        print(list1)
        print(list2)

        for i in range( len(list1) and len(list2)):
            temp1 = list1[i]
            temp2 = list2[i]
            if(len(temp1) == len(temp2)):
                gap1 = 0;
                gap2 = 0;
                for j in range(len(temp1)-totalgap):

                    if(j < num):
                        print("check") 
                    
                    elif(temp1[j] == temp2[j]):
                        score = score + match

                    else:
                        totalgap = abs(gap1 - gap2)
                        for k in range( len(temp1)- j-totalgap):
                            endgap = endgap + 1 
                            if( temp1[j+k] == temp2[j+k]):
                                score = score + (mismatch*k)
                                endgap = 0
                                num =j + k
                                break
                            elif( temp1[j] == temp2[j+k]):
                                score = score + (gap*k)
                                gap2 = gap2 + k
                                endgap = 0
                                num = j + k
                                break
                            elif(temp1[j+k] == temp2[j]):
                                score = score + (gap*k)
                                gap1 = gap1 + k
                                endgap = 0
                                num = j + k
                                break
                    print(score, num  , temp1[j], temp2[j])
                    if(endgap > 0 ):
                         score = score + (gap*endgap)
                       


            else:  
                shorter = ""
                longer = ""
              
                    
                if(temp1 > temp2):
                    longer = temp2
                    shorter = temp1
                elif(temp1 < temp2):
                    longer = temp1
                    shorter = temp2
                for j in range( len(shorter)):
                    gap1 = 0;
                    gap2 = 0;
                    
                    if(j < num):
                      print("check") 

                    elif( longer[j] == shorter[j]):
                        score = score + match
                    else:
                        totalgap = abs(gap1 - gap2)
                        for k in range( len(shorter)- (j-totalgap)):
                            endgap = endgap+1
                            if( longer[j+k] == shorter[j+k]):
                                score = score + (mismatch*k)
                                endgap=0
                                num =j + k
                                break
                            elif( longer[j] == shorter[j+k]):
                                score = score + (gap*k)
                                gap2 = gap2 + k
                                endgap = 0;
                                num =j + k
                                
                                break
                            elif(longer[j+k] == shorter[j]):
                                score = score + (gap*k)
                                gap1 = gap1 + k
                                endgap = 0;
                                num =j + k
                                break
                       
                        if(endgap > 0 ):
                            score = score + (gap*endgap)

                score = score + (  (len(longer) - len(shorter))*gap)
            print("endgap " , endgap)
            print("score: " , score)
            print("totalgap " , totalgap)
            print(temp1)
            print(temp2)
            num = 0 
            endgap = 0
            score = 0

        if(len(list1) > len(list2)):
            num = len(list1) - len(list2)
        elif(len(list1) < len(list2)):
            num = len(list2) - len(list1)

        for i in range (num+1 , len(list1)):
            temp1 = list1[i]
            score = score + ( len(temp1)*gap)
            totalgap = totalgap + len(temp1)
            print("score: " , score)
            print("totalgap " , totalgap)
            print(temp1)



                            
                        

DivideConquer(s1, s2)
