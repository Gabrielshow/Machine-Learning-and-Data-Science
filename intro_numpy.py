#python for data science
import numpy as np

#creating a numpy array
x = np.arange(1, 7)

#a 1-dimensional array containing six elements
#to reshape the array we use the reshape() method
z = x.reshape(3,2)
print(z)

#indexing and slicing
y = np.arange(1,10)
print(x[0:2])
print(y[5:])

#conditions can also be provided as the index to elements
p = np.arange(1,10)
print(p[p<4])
print(p[(p>5)&(p%2==0)])

#array operations
print(p.sum())

#statistics
print(np.mean(p))
print(np.median(p))
print(np.var(p))
print(np.std(p))