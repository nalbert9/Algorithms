#!/usr/bin/env python
def binary_search(list_elements, item):
    low = 0
    high = len(list_elements)

    while (low <= high):
        middle = (low + high)//2
        guess = list_elements[middle]

        if (guess == item):
            return middle
        elif (guess > item):
            high = middle - 1
        else:
            low = middle + 1
    return None

if __name__=='__main__':
    my_list = [1, 2, 3, 5, 7, 10, 40]
    print(binary_search(my_list, 5))