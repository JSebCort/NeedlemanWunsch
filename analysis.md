---
layout: default
title: Analysis
---
# Analysis on our implementation of algorithms

|     Algorithm    | Time (seconds) | Runtime <br> (n = length of first sequence, m = length of second sequence) |           Input that lead to the correct alignment          |
|:----------------:|:--------------:|:--------------------------------------------------------------------:|:-----------------------------------------------------------:|
|    Brute Force   |    0.440652    |             Best Case: O(n<sup>2</sup>) or O(nm) <br> Worst Case: O(n<sup>3</sup>)            |          AGTCTA <br> AGTTA <br> Alignment: AGT-TA <br> Score: 3          |
| Needleman-Wunsch |    0.678185    |                                 O(nm)                                |       ATGTAGTGTATAAAGTACATGCA <br> ATGTAGTACATGCA <br> Score: -4      |
|      Greedy      |      0.001     |             Best Case: O(n<sup>2</sup>) or O(nm) <br> Worst Case: O(n<sup>3</sup>)            |                ACGTCAGGG <br> ACGTCAGGC <br> Score: 8                |
|      Random      |    11.16014    |                                O(n<sup>2</sup>)                                | ATGTAGTGTATAAAGTACAATGCA <br> ATGTAGTACATAAAGTCCGCTGCA <br> Score: 14 |

![Picture](Images/grap.PNG)


[Further Analysis in PDF](Documentation/Bioinformatics%20Project%202%20QA%20Test%20Cases%20and%20Known%20Issues.pdf)

[Head back to the Main Page](https://jsebcort.github.io/NeedlemanWunsch/)
