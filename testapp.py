# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:40:44 2019

@author: bhatt
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from randomforest import saved_model

a = [1,	5,	'Semester 1, Semester 2, Semester 3, Semester 4',	1,	1,	8,	0,	0.5,	1,	2.0,	1.0,	0,	7,	3,	1,	4,	1,	0.5,	0.0,	1.0,	8,	0
]

X = pd.DataFrame(a)
X = X.transpose()

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
LabelEncoder_X = LabelEncoder()
#X[:, 2] = LabelEncoder_X.fit_transform(X[:, 2])
X.values[:, 2] = LabelEncoder_X.fit_transform(X.values[:, 2])

reg= pickle.loads(saved_model)
y_pred=reg.predict(X)