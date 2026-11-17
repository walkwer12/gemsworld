# #AIM 5: Write a program to demonstrate Divide and Conquer approach using Closest pair of points. 
import math
def closest(p):

    #first check whether there are less points in the list. If yes we can directly find the closest pair
    if len(p) <= 3:
        d = float('inf')
        pair = None

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                dist = math.dist(p[i], p[j])

                if dist < d:
                    d = dist
                    pair = (p[i], p[j])
        return d, pair
    
 #but in the case that there are more than 3 pairs then do this. 
    mid = len(p) // 2

    left_d, left_pair = closest(p[:mid]) #left half
    right_d, right_pair = closest(p[mid:]) #right half

    d, pair = (left_d, left_pair) if left_d < right_d else (right_d, right_pair)

    mid_x = p[mid][0]

    strip = []

    for point in p:
        if abs(point[0] - mid_x) < d:
            strip.append(point)

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            dist = math.dist(strip[i], strip[j])

            if dist < d:
                d = dist
                pair = strip[i], strip[j]

    return d, pair

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

distance, pair = closest(points)

print("Closest pair:", pair)
print("Smallest distance:", distance)






















# import math

# def closest(p):
#     if len(p) <= 3: #checks whether the list contains 3 pairs or less. If yes, we directly calculate the distances between every possible pair.
#         d = float('inf')
#         pair = None

#         for i in range(len(p)):
#             for j in range(i + 1, len(p)): #this is done so that we don't repeat grouping the same pair of points again. 
#                 dist = math.dist(p[i], p[j])
#                 if dist < d:
#                     d = dist
#                     pair = (p[i], p[j])

#         return d, pair

#     mid = len(p) //2 #finds the middle index of the list of points. 

# #divides the list of points into two halves and recursively calls the closest function on both halves.
#     left_d, left_pair = closest(p[:mid])
#     right_d, right_pair = closest(p[mid:])

#     d, pair = (left_d, left_pair) if left_d < right_d else (right_d, right_pair)

#     mid_x = p[mid][0] #we do this to find points close to the dividing line

#     strip = [] #store points near the dividing list here

#     for point in p:
#         if abs(point[0] - mid_x) < d:
#             strip.append(point)

#     for i in range(len(strip)):
#         for j in range(i + 1, len(strip)):
#             dist = math.dist(strip[i], strip[j])
#             if dist < d:
#                 d = dist
#                 pair = (strip[i], strip[j])

#     return d, pair

# points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

# points.sort() #sort the points based on x-coordinate

# distance, points = closest(points)

# print("Closest pair:", points)
# print("Smallest distance:", distance)


