
















































































import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    return quicksort(left) + equal + quicksort(right)
arr = list(map(int, input("Enter numbers: ").split()))
print("Sorted array:", quicksort(arr))
