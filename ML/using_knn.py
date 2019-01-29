# knn
from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data
y=iris.target
print(x.shape)
print(y.shape)

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(x,y)
a=[4,5,6,2]
print(knn.predict([a]))

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
print(logreg.fit(x,y))
print(logreg.predict([a]))
