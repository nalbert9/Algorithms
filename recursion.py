#!usr/bin/env python
"""
A recursion algorithm is one where the algorithm calls on itself 
but using iteratively simpler and smaller values or structures
"""
# n! = n × (n−1)!
# 4! = 4 × 3 × 2 × 1 = 24
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

if __name__=="__main__":
    print(factorial(9))