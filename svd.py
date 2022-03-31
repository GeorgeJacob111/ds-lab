import numpy as np
from scipy.linalg import svd
a=np.array([[1,2,5,5,5],[2,6,6,6,6],[6,5,8,8,8],[7,8,9,9,9]])
print(a)
U,S,VT=svd(a)
print(f"Decomposed mattrix is\n{U}\n")
print(f"inverse mattrix is \n{S}\n")
print(f"Transpose mattrix is \n{VT}\n")