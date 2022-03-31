from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

datas = load_iris()
x= datas.data
y= datas.target

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=101,test_size=0.4)

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train,y_train)

pred = knn.predict(x_test)

p = [[10,2.3,104,15]]

print(knn.predict(p))
print(accuracy_score(pred,y_test))