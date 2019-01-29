# SVM using scikit-learn

from sklearn import svm     # importing the SVM model
from sklearn import datasets  # importing a sample data(iris data)
from sklearn.cross_validation import train_test_split

var = datasets.load_iris()  # loading the iris dataset into a variable
print(type(var), '\n')
print(var, '\n')   # prints both the data and the target
print(var.data, '\n')    # prints only the data
print(var.feature_names, '\n')   # shows the feature names of the dataset
print(var.target_names, '\n')

x = var.data[:, 2]   # all rows of the first two columns of the data
y = var.target

# splitting the training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# converting all the arrays into one direction
print(x_test.shape)
x_train_mod = x_train.reshape(-1, 1)
print(x_train_mod.shape)
x_test_mod = x_test.reshape(-1, 1)
y_train_mod = y_train.reshape(-1, 1)
y_test_mod = y_test.reshape(-1, 1)

model = svm.SVC(kernel='linear')
model.fit(x_train_mod, y_train_mod)

y_pred_mod = model.predict(x_test_mod)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test_mod, y_pred_mod)
print(accuracy)
