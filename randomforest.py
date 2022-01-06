#Importing dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
dataset = pd.read_csv('ProjectData.csv')
data=dataset.drop(dataset.columns[[0,1,2,3,26]], axis=1)  


X = dataset.iloc[:, 4:26].values
Y = dataset.iloc[:, 3].values
xData = pd.DataFrame(X);
yData = pd.DataFrame(Y);

# Saving feature names for later use
data_list = list(data.columns)


#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncoder_X = LabelEncoder()
X[:, 2] = LabelEncoder_X.fit_transform(X[:, 2])


#Splitting dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
x_testData = pd.DataFrame(X_test);
x_trainData = pd.DataFrame(X_train);
y_testData = pd.DataFrame(Y_test);
y_trainData = pd.DataFrame(Y_train);


# Fitting Random forest to the training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state=0)
regressor.fit(X_train,Y_train)

saved_model=pickle.dumps(regressor)
