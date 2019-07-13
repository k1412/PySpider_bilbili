import numpy as np 

a = np.random.random(12).reshape(3,4)
print a
b = np.split(a, 2, axis=1)
print '\n'
print b