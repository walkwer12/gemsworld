


























































#Implement divide and conquer algorithm - Strassens Algorithm

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

def strassen(A, B):
    if len(A) == 1:
        return A * B
    
    #For matrix A in order to form [a  b]
                                  # [c  d]
    
    a, b = A[:1, :1], A[:1, 1:]
    c, d = A[1:, :1], A[1:, 1:]
    
    #now for matrix B to form [e   f, g   h]
    e, f = B[:1, :1], B[:1, 1:]
    g, h = B[1:, :1], B[1:, 1:]
    
    #now performing the individual multiplications
    
    p = strassen(a + d, e + h)
    q = strassen(c + d, e)
    r = strassen(a, f - h)
    s = strassen(d, g - e)
    t = strassen(a + b, h)
    u = strassen(c - a, e + f)
    v = strassen(b - d, g + h)
    c11 = p + s - t + v
    c12 = r + t
    c21 = q + s
    c22 = p + r - q + u
    
    row1 = np.hstack((c11, c12))
    row2 = np.hstack((c21, c22))
    
    return np.vstack((row1, row2))

print("Result: ")
print(strassen(A, B))
    
    