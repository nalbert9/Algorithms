#!/usr/bin/env python
"""
The binary_search function takes a sorted array and an item. If the
item is in the array, the function returns its position.
"""
def binary_search(list_elements, item):
    low = 0
    high = len(list_elements)

    while (low <= high):
        # Each time, you check the middle element
        middle = (low + high)//2
        guess = list_elements[middle]

        # If the guess is too low, you update low
        # And if the guess is too high, you update high
        if (guess == item):
            return middle
        elif (guess > item):
            high = middle - 1
        else:
            low = middle + 1
    return None
    # Running time O(log n)

if __name__=='__main__':
    my_list = [1, 2, 3, 5, 7, 10, 40]
    print(binary_search(my_list, 5))
