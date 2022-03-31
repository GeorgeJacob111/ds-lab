import matplotlib.pyplot as plt
from sklearn import datasets,linear_model,metrics
from sklearn.model_selection import train_test_split
boston=datasets.load_boston()
x=boston.data
y=boston.target

x_train,x_test,y_train,y_test=train_test_split( x,y,test_size=0.4,random_state=1)
reg=linear_model.LinearRegression()
reg.fit(x_train,y_train)
pre=reg.predict(x_test)
print("Prediction : ",pre)
print('Coefficients: ',reg.coef_)
print('Variance Score:{}'.format(reg.score(x_test,y_test)))
