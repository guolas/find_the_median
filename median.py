#!/bin/python3

import random

def find_median(A):
    N = len(A)
    """
    The anchor is always the point in the middle
    """
    mid_idx = int((N - 1) / 2)
    start_anchor = A[mid_idx]

    lower = []
    higher = []
    equal = []
  
    for ii in range(N):
        if A[ii] > start_anchor:
            higher.append(A[ii])
        elif A[ii] == start_anchor:
            equal.append(A[ii])
        else:
            lower.append(A[ii])
    new_A = lower + equal + higher
    end_anchor = new_A[mid_idx]

    if start_anchor == end_anchor:
        median = start_anchor
    else:
        median = find_median(new_A)
    return median

"""
Get the size of the array
"""
N = int(input().strip())

"""
Get the array
"""
A = [int(x) for x in input().strip().split(" ")]

median = find_median(A)
print(str(median))
