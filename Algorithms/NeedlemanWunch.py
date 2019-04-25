import re
import collections
import csv
import sys 
import numpy as np
from string import *



#s1 = input('Enter a file name: ')
list1 = "ATGTAGTGTATAAAGTACATGCA"
#s2 = input('Enter a file name: ')
list2 = "ATGTAGTACATGCA"
match = 1
mismatch = -1
gap = -2

Zeros = [len(s1)][len(s2)]
Matrix = [len(s1)][len(s2)]

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



def NeedlemanWunch(s1,s2,match ,mismatch , gap ):
    penalty = {'MATCH': match, 'MISMATCH': mismatch, 'GAP': gap} #A dictionary for all the penalty valuse.
    n = len(s1) + 1 #The dimension of the matrix columns.
    m = len(s2) + 1 #The dimension of the matrix rows.
    al_mat = np.zeros((m,n),dtype = int) #Initializes the alighment matrix with zeros.
    p_mat = np.zeros((m,n),dtype = str) #Initializes the alighment matrix with zeros.
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
    print (np.matrix(al_mat))
    print (np.matrix(p_mat))
    
    path = ""
    score = 0
    i = m-1
    j = n-1
    while( i > 0 and j > 0):
        if(al_mat[i-1][j] > al_mat[i-1][j-1] and al_mat[i-1][j] > al_mat[i][j-1]):
            i = i - 1
            s2 = s2[:i+j] + '-' + s2[i+j:]
            
                
        elif(al_mat[i][j-1] > al_mat[i-1][j-1] and al_mat[i][j-1] > al_mat[i-1][j]):
            j = j - 1
            s2 = s2[:i+j] + '-' + s2[i+j:]
                
        elif(al_mat[i-1][j-1] > al_mat[i][j-1] and al_mat[i-1][j-1] > al_mat[i-1][j]):
            i = i - 1
            j = j - 1
             
            
    
    print("check")
    print(s1)
    print(s2)
    score = al_mat[m-1][n-1]
    print(score)

    return(s2 , score)

NeedlemanWunch(list1, list2, match, mismatch, gap)





