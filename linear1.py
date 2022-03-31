import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import LinearRegression

x=np.array([5,12,25,35,45,55]).reshape(-1,1)
y=np.array([5,20,16,32,22,38])
print(x)
model = LinearRegression()
model.fit(x,y)
s=model.score(x,y)
print("coefficient",s)
print("intercept",model.intercept_)
print("slop",model.coef_)

y_pred = model.predict(x)
print("predict",y_pred)

pl.scatter(x,y)
pl.plot(x,y_pred)
pl.show()
