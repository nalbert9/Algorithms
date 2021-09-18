#!usr/bin/env python

"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning.
"""
# Function to find the smallest element in array
def find_smallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

# Use this function to write selection sort
def selection_sort(arr):
    new_arr = []
    for i in range (len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

 # Running time O(n^2)

if __name__ =='__main__':
    example = [5, 12, 8, 45, 49, 2, 3]
    print(selection_sort(example))
