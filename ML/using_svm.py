# scikit learn
# SVM classifier

from sklearn import svm
from sklearn import datasets  # default dataset of scikit learn
iris=datasets.load_iris()
print(type(iris))
print(iris.feature_names)
print(iris.data)
print(iris.target_names)      # categories to be classified in
print(iris.target)            # prediction

x=iris.data[:,2]  # independent variable
y=iris.target     # dependent variable

# splitting data into training data and testing data
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)

x_train_mod=x_train.reshape(-1,1)
x_test_mod=x_test.reshape(-1,1)
y_train_mod=y_train.reshape(-1,1)
y_test_mod=y_test.reshape(-1,1)

model=svm.SVC(kernel='linear')
model.fit(x_train_mod,y_train_mod)
y_pred_mod=model.predict(x_test_mod)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test_mod,y_pred_mod))

