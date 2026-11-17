


































































import random
n = int(input("Enter number of points: "))
inside = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        inside += 1
pi = 4 * inside / n
print("Estimated value of Pi:", pi)
