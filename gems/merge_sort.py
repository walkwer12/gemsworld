











































































#Write a program to demonstrate Log-Linear O(n log n) Time Complexity (Merge Sort).

import time

start = time.time()

def merge(a, b):
    result = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))

    result.extend(a)
    result.extend(b)

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr #to stop implementation

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [20, 2, 9, 7, 12, 15, 16, 8]
sorted_arr = merge_sort(arr)

print("Unsorted Array:", arr)
print("Sorted Array:", sorted_arr)

end = time.time()
print("Execution Time:", end - start)