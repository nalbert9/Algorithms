#!usr/bin/env python
"""
Quicksort is a sorting algorithm. It use Divide and conquer.
To solve a problem using D&C, there are two steps:
    1. Figure out the base case. This should be the simplest possible case.
    2. Divide or decrease your problem until it becomes the base case.
"""
def quick_sort(elements):

    n = len(elements)
    if n < 2:
        return elements        # Arrays with 0 or 1 element are already sorted
    else:
        pivot = elements[0]
        less = []
        greater = []

        for i in range(1, n):
            if pivot <= elements[i]:
                greater.append(elements[i])
            if pivot > elements[i]:
                less.append(elements[i])

        # The Pythonic way :) 
        # less = [i for i in elements[1:] if i <= pivot] # Sub-array of all the elements less than the pivot
        # greater = [ i for i in elements[1:] if i > pivot] # Sub-array of all the elements greater than the pivot 

        return quick_sort(less) + [pivot] + quick_sort(greater)
        # Running time O(log n)

if __name__ =='__main__':
    example = [27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12,99 ]
    print(quick_sort(example))