


import numpy 
import pandas as pd
from sklearn import linear_model

df=pd.read_csv('SaYoPillow.csv')

from sklearn.model_selection import train_test_split
x = df.drop(columns='sl',axis=1)
y=df['sl']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)






