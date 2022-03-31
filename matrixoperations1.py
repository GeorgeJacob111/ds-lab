import numpy as num
m1 = num.array([[10,20],[30,40]])
m2 = num.array([[10,20],[30,40]])

print("First matrix : \n", m1)
print("Second matrix : \n", m2)

add = num.add(m1,m2)
print("addition :- \n",add)

sub = num.subtract(m1,m2)
print("subrtaction :- \n",sub)

div = num.divide(m1,m2)
print("division :- \n",div)

mul = num.multiply(m1,m2)
print("multiplication :- \n",mul)

sqrt1 = num.sqrt(m1)
print("sqrt1 :- \n",sqrt1)

sqrt2 = num.sqrt(m2)
print("sqrt2 :- \n",sqrt2)

sum1 = num.sum(m1)
print("sum1 :- \n",sum1)

sum2 = num.sum(m2)
print("sum2 :- \n",sum2)

dot1 = num.dot(m1,m2)
print("dot :- \n",dot1)

print("transpose of matrix m1 is: ",m1.T)
print("transpose of second matrix is: ",m2.T)