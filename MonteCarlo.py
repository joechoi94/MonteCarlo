import random
import numpy as np

count = 0
N = 100000
for i in range (N):
    x = float(np.random.uniform(-1,1))
    y = float(np.random.uniform(-1,1))
    r = (x**2 + y**2)**(0.5)
    if r >=0.5 and r <= 1 :
        count +=1

A_computed = 4*float(count)/N
A_real = np.pi - ((0.5)**2)*(np.pi)
E = abs(A_computed - A_real)/float((A_real))
print(A_real)
print(A_computed)
print(E)
