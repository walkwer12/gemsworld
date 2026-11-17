#Write a program to demonstrate Linear Time Complexity O(n) - (Bubble Sort).
import time
arr = [64, 34, 25, 12, 22, 11, 90]
start = time.time()
print("Unsorted array:", arr)

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 -i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


print("Sorted array:", arr)
end = time.time()
print("Time taken:", end - start, "seconds")
