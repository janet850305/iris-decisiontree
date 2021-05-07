# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, test_size=0.3)###30%的data作為testing


clf = tree.DecisionTreeClassifier()
iris_clf = clf.fit(train_x, train_y)
test_y_predicted = iris_clf.predict(test_x)
###print(test_y_predicted)
###print(test_y)
t = 0
f = 0
for i in range(len(test_y_predicted)):

    if (test_y_predicted[i]==test_y[i]):
        t = t + 1
    else:
        f = f + 1
print("true:",t,"  false:",f)
    
    
