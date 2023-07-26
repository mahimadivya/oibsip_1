# -*- coding: utf-8 -*-
"""iris_flower_classification_Task-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18jqCra0e8cc4bwE5Smj6457l-EaSaYT5
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

df= pd.read_csv('Iris.csv')

df.head()

df.tail()

df.shape

df.dtypes

df.info()

df.describe()

df.isnull().sum()

data=df.groupby('Species')

data.head()

df['Species'].unique()

df.info()

plt.boxplot(df['SepalLengthCm'])

plt.boxplot(df['SepalWidthCm'])

plt.boxplot(df['PetalLengthCm'])

plt.boxplot(df['PetalWidthCm'])

sns.heatmap(df.corr())

df.drop('Id',axis=1,inplace=True)

sp={'Iris-setosa':1,'Iris-versicolor':2,'Iris-virginica':3}

df.Species=[sp[i] for i in df.Species]

df

X=df.iloc[:,0:4]
X

y=df.iloc[:,4]
y

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)

model=LinearRegression()

model.fit(X,y)

model.score(X,y)

model.coef_

model.intercept_

y_pred=model.predict(X_test)

print("Mean squared error: %.2f" % np.mean((y_pred - y_test) ** 2))