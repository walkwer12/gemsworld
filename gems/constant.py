#AIM 1: Write a Program to demonstrate constant time complexity O(1).
import time

start = time.time() * 1000
arr = [5, 25, 4, 10, 7, 120, 43, 65]

for i in range(len(arr)):
    if arr[i] == 120:
        print("Element found at index:", i)
        break

end = time.time() * 1000
print("Time taken:", end - start, "seconds")
