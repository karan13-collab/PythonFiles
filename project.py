# -*- coding: utf-8 -*-
"""Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIT1vcjzoZ-VL5FyrkvQt85-d_IutctE
"""

import sys
print('Python: {}'.format(sys.version))
import scipy
print('Scipy: {}'.format(scipy.__version__))
import numpy
print('numpy: {}'.format(numpy.__version__))
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('pandas: {}'.format(pandas.__version__))
import sklearn
print('Sklearn: {}'.format(sklearn.__version__))

import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import  pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import LabelEncoder

#loading the data
data = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'class']
dataset = read_csv(data,names=names)

#dimensions of the dataset
print(dataset.shape)

print(dataset.head(10))

#statistical summary
print(dataset.describe())

#class distribution
print(dataset.groupby('class').size())

#univariate plots - box and whisker plot
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

#histogram of the variable
dataset.hist()
pyplot.show()

#multivariate plots
scatter_matrix(dataset)
pyplot.show()

#creating a validation set
#splitting dataset
array = dataset.values
X = array[:,0:2]
Y = array[:,2]
X_train, X_validation, Y_train, Y_validation = train_test_split(X,Y,test_size = 0.2, random_state=1)

#logistic regression
#linear discriminant analysis
#K-nearest neighbors
#classification and regression trees
#gaussian naive bayes
#svm

#building models
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

#EVALUATE THE CREATED MODEL
results = []
names = []
for name, model in models:
  kfold = StratifiedKFold(n_splits=10, random_state=1)
  cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
  names.append(name)
  print('%s: %f (%f)' % (name,cv_results.mean(), cv_results.std()))

#compare models
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparision')
pyplot.show()

#predictions on svm
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

#evaluate our predictions
print(accuracy_score(Y_validation, predictions)
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))