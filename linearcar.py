import pandas
from sklearn.linear_model import LinearRegression

df=pandas.read_csv("cars.csv")
x=df[['Weight','Volume']]
y=df['cyl']
regr=LinearRegression()
regr.fit(x,y)
predictedco2=regr.predict([[2300,1300]])
print(predictedco2)