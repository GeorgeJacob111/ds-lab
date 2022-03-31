from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as pl

idata=load_iris()
X=idata.data
Y=idata.target
#print(X)
#print(Y)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.4,random_state=101)
knn=KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train,Y_train)
Y_pred=knn.predict(X_test)
p=[[6.5,9.,9.2,2.]]
print(f"prediction for [6.5,9.,9.2,2.] is {knn.predict(p)}")
print(f"accuracy of the algorithm {accuracy_score(Y_test,Y_pred)}")