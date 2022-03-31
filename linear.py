import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pl

x=np.array([5,12,25,35,45,55]).reshape(-1,1)
y=np.array([5,20,16,32,22,38])
print(x)
model=LinearRegression()
model.fit(x,y)
r_sq=model.score(x,y)
print('coefficent of determination',r_sq)
print("intercept",model.intercept_)
print("slope",model.coef_)

y_pred=model.predict(x)
print('predicted value',y_pred)

pl.scatter(x,y)
pl.plot(y_pred)
pl.show()