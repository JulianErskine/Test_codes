import numpy as np
import scipy as sp

x=5
print 'My X =',x

J = np.asmatrix(np.array([[1.0, 2, 9],[4,5,6]]))

print 'J = ',J

q = np.asmatrix(np.array([1,2,3]))

print 'q = ',q

X1 = J * q.T

print 'X1 = ', X1
