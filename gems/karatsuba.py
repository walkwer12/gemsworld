
























































































#AIM: Write a program to demonstrate the Divide and Conquer approach using Karatsuba multiplication for large numbers.

def karatsuba(x, y):
    
    #stopping condition
    if x < 10 or y < 10:
        return x * y
    
    #find out the maximum no. of digits
    n = max(len(str(x)), len(str(y)))
    
    m = n // 2 #floor division
    
    p = 10 ** m #power - multiplying 10 exponentially with the half of max no. of digits
    
    #divide the numbers into halves
    a, b = divmod(x, p)
    c, d = divmod(y, p)
    
    z0 = karatsuba(b, d)
    z2 = karatsuba(a, c)
    z1 = karatsuba(a+b, c+d) -z2 - z0
    
    return z2*p*p + z1*p + z0

print(karatsuba(7894, 3421))
    
    
    

































# def karatsuba(x, y):
#     if x < 10 or y < 10:
#         return x * y

#     n = max(len(str(x)), len(str(y)))
#     m = n // 2
    
#     p = 10 ** m #exponential
    
#     #split the numbers
#     a, b = divmod(x, p)
#     c, d = divmod(y, p)
    
#     z0 = karatsuba(b, d) #right half
#     z2 = karatsuba(a, c) #left half
#     z1 = karatsuba(a + b, c + d) - z2 - z0
    
#     return z2*p*p + z1*p + z0

# print(karatsuba(1234, 5678))