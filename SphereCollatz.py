#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

values = {}

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    itemp = i
    jtemp = j
    a = 1
    assert (i>0 and i<1000000) and (j>0 and j<1000000)
    if (i>j):
        tmp = i
        i = j
        j = tmp
        itemp = i
        jtemp = j
    diff = j - i
    while (diff != -1):
        current = j - diff
        if current not in values:
            length = collatz_eval_helper(current)
        else:
            length = values[current]
            if length > a:
                a = length
            diff -= 1
    assert a > 0
    assert i == itemp
    assert j == jtemp
    return a

def collatz_eval_helper (diff):
    """
    recursively go to lowest value by collatz for diff
    work upwards to fill in later cache spots
    """
    if diff not in values:
        if diff == 1:
            values[diff] = 1
        elif diff % 2 == 1:
            values[diff] = collatz_eval_helper(3 * diff + 1) + 1
        else:
            temp = diff >> 1
            values[diff] = collatz_eval_helper(temp) + 1
    return values[diff]

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

import sys

from Collatz import collatz_solve

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

