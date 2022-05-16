#!/usr/bin/env python

def bubble_sort(elements):
    n = len(elements)

    # Traverse through all array elements
    for i in range(n-1):

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements


# Running time O(n^2)
if __name__ == "__main__":
    example = [5, 12, 8, 45, 49, 2, 3]
    print(bubble_sort(example))