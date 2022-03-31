import numpy as n
from scipy.linalg import svd

ar = n.array([[1,2,5,5,5],[2,6,6,6,6],[6,5,8,8,8],[7,8,9,9,9]])
print(ar)

d,i,t = svd(ar)

print("Decomposed matrix is\n",d)
print("inverse matrix is\n",i)
print("transpose matrix is\n",t)