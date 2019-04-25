---
layout: default
title: Analysis
---
# Analysis on our implementation of the Needleman-Wunsch Algorithm

|     Algorithm    | Time (seconds) | Runtime(n = length of first sequence, m = length of second sequence) |           Input that lead to the correct alignment          |
|:----------------:|:--------------:|:--------------------------------------------------------------------:|:-----------------------------------------------------------:|
|    Brute Force   |    0.440652    |             Best Case: O(n<sup>2</sup>) or O(nm) Worst Case: O(n<sup>3</sup>)            |          AGTCTA, AGTTA  Alignment: AGT-TA Score: 3          |
| Needleman-Wunsch |    0.678185    |                                 O(nm)                                |       ATGTAGTGTATAAAGTACATGCA ATGTAGTACATGCA Score: -4      |
|      Greedy      |      0.001     |             Best Case: O(n<sup>2</sup>) or O(nm) Worst Case: O(n<sup>3</sup>)            |                ACGTCAGGG ACGTCAGGC  Score: 8                |
|      Random      |    11.16014    |                                O(n<sup>2</sup>)                                | ATGTAGTGTATAAAGTACAATGCA ATGTAGTACATAAAGTCCGCTGCA Score: 14 |

![Picture](Images/grap.PNG)

[Head back to the Main Page](https://jsebcort.github.io/NeedlemanWunsch/)
