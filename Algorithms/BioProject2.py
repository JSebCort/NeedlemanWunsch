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

def Greedy(s1, s2):#finds the fastest soluion 
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

    if(s1 == s2):#if  strings are exactly the same 
        print(s1)
        print(s2)
        print("score" + len(s1))

    elif(len(s1) == len(s2)):#if theyre the same length loops throught 
        for i in range(len(s1)):
            if(s1[i]==s2[i]):# if characters match add 1 to match 
                score += match
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

    print("Greedy")
    print(best1)
    print(best2)
    print("Score: " , max)              
                

Greedy(list1,list2)



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
    

    if(s1 == s2):#inf thy are the same 
        print(s1)
        print(s2)
        print("score: " + len(s1))

    elif(len(s1) == len(s2)):#if they are the same length

        for i in range(len(s1)-1):
            if(s1[i]==s2[i]):
                score += match
            else:
                tmp = score
                for j in range ((len(s1)-i)-1):

                    if(s1[i]==s2[i+j]):# checks for gaps
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
                        i += j
                        break

                    elif(s1[i+j]==s2[i]):# checks for gaps
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
            else:
                tmp = score
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

                    elif(s1[i]==s2[i+j]):
                        score += gap*j
                        for k in range (j):
                            s1 = s1[:i+k] + '-' + s1[i+k:]
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
            else:
                tmp = score
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
        if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
        score = 0
        s1 = temp1
        s2 = temp2

                    

    else: #if the strings are not the same length

          for i in range(len(s1)-1):# runs similar loops to check all possible combinations 
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
          if(score > max):# keeps track of highest score for comapred strings 
            max = score
            best1 = s1
            best2 = s2
          score = 0
          s1 = temp1
          s2 = temp2

                   
    print("brutforce")
    print(best1)
    print(best2)
    print("Score: " , max)


brutForce(list1,list2)



def Diagonal(n1,n2,pt):
    if(n1 == n2):
        return pt['MATCH']
    else:
        return pt['MISMATCH']


#This function gets the optional elements of the aligment matrix and returns the elements for the pointers matrix.
def Pointers(di,ho,ve):

    pointer = max(di,ho,ve) #based on python default maximum(return the first element).

    if(di == pointer):
        return 'D'
    elif(ho == pointer):
        return 'H'
    else:
         return 'V' 



def NW(s1,s2,match = 1,mismatch = -1, gap = -2):
    penalty = {'MATCH': match, 'MISMATCH': mismatch, 'GAP': gap} #A dictionary for all the penalty valuse.
    n = len(s1) + 1 #The dimension of the matrix columns.
    m = len(s2) + 1 #The dimension of the matrix rows.
    al_mat = data.zeros((m,n),dtype = int) #Initializes the alighment matrix with zeros.
    p_mat = data.zeros((m,n),dtype = str) #Initializes the alighment matrix with zeros.
    #Scans all the first rows element in the matrix and fill it with "gap penalty"
    for i in range(m):
        al_mat[i][0] = penalty['GAP'] * i
        p_mat[i][0] = 'V'
    #Scans all the first columns element in the matrix and fill it with "gap penalty"
    for j in range (n):
        al_mat[0][j] = penalty['GAP'] * j
        p_mat [0][j] = 'H'
    #Fill the matrix with the correct values.

    p_mat [0][0] = 0 #Return the first element of the pointer matrix back to 0.
    for i in range(1,m):
        for j in range(1,n):
            di = al_mat[i-1][j-1] + Diagonal(s1[j-1],s2[i-1],penalty) #The value for match/mismatch -  diagonal.
            ho = al_mat[i][j-1] + penalty['GAP'] #The value for gap - horizontal.(from the left cell)
            ve = al_mat[i-1][j] + penalty['GAP'] #The value for gap - vertical.(from the upper cell)
            al_mat[i][j] = max(di,ho,ve) #Fill the matrix with the maximal value.(based on the python default maximum)
            p_mat[i][j] = Pointers(di,ho,ve)
    print (data.matrix(al_mat))
    print (data.matrix(p_mat))



NW(list1,list2)