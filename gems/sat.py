



































































#AIM 1: SAT
from itertools import product 
 
def sat(): 
    for a,b in product([0,1], repeat=2): 
        if (a or b) and (not a or b): 
            return True 
    return False 
 
print("SAT:", sat()) 
print("Unsatisfiable:", not sat())

#AIM 2: 2-SAT
from itertools import product 
def check(clauses, n): 
    for vals in product([False, True], repeat=n): 
        if all(any(vals[abs(x)-1] == (x > 0) for x in c) 
               for c in clauses): 
            return True 
    return False 
 
print("2-SAT:", check([[1, -2], [-1, 2]], 2)) 
print("Unsatisfiable:", not check([[1], [-1]], 1)) 

#AIM 3: 3-SAT 
from itertools import product 
def check(clauses): 
    return any( 
        all(any(vals[abs(x)-1] == (x > 0) for x in c) 
            for c in clauses) 
        for vals in product([False, True], repeat=3) 
    ) 
print("3-SAT:", check([[1, 2, 3], [-1, 2, 3]])) 
print("Unsatisfiable:", not check([[1], [-1]]))


