


import numpy 
import pandas as pd
from sklearn import linear_model

df=pd.read_csv('SaYoPillow.csv')

reg=linear_model.LinearRegression()
reg.fit(df[['sr','rr','t','lm','bo','rem','sr.1','hr']],df.sl)

sr=float(input("Enter snoring rate"))
rr=float(input("Enter respiration rate"))
t=float(input("Enter body temperature"))
lm=float(input("Enter limb movement"))
bo=float(input("Enter blood oxygen"))
rem=float(input("Enter eye movement"))
sr1=float(input("Enter sleeping hours"))
hr=float(input("Enter heart rate"))

print("Your Stress Rate is",int(reg.predict([[sr,rr,t,lm,bo,rem,sr199,hr]])))






