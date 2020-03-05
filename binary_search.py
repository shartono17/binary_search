#!/bin/python3

import math

def find_smallest_positive(xs):

    #xs.sort()
    left = 0
    right = len(xs)-1
    def binsort(left, right):
        mid=(left+right)/len(xs)
        if 0 <xs[mid]: right = mid-1
        if 0 > xs[mid]: left = mid+1
        if 0 == xs[mid]: return mid+1
        if left == right < 0: return None
    return binsort(left,right)

    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST
    Find the index of the smallest positive number.
    If no such index exists, return 'None'
    
    HINT:
    This is essentially the binary search algorithm from class, 
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''


def count_repeats(xs, x):
    upper = x+1
    lower = x-1

    left = 0
    right = len(xs)-1

    if len(xs) == 0: return False
    def binsort(left,right, val):
        mid = (left+right)/len(xs)
        if val < xs[mid]: right = mid-1
        if val> xs[mid]: left = mid+1
        if val == xs[mid]: return mid
        if left == right: return None

    upbound = binsort(left, right, upper)
    lowerbound = binsort(left, right, lower)
    freqcount = upperbound - lowerbound
    return freqcount
   

    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''


def argmin(f, lo, hi, epsilon=1e-3):

    if math.abs(hi-lo) < epsilon: return lo
    else: 
        m1 = math.uniform(lo, hi)
        m2 = math.uniform(lo,hi)
        if m2< m1:


    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''


