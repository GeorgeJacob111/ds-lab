from tensorflow import keras
print('tensorflow/Keras: %s' %keras.__version__)

from keras.models import Sequential
from keras import Input
from keras.layers import  Dense

import pandas as pd
print('pandas : %s' %pd.__version__)
import numpy as np
print('pandas : %s' %np.__version__)

import sklearn
print('sklearn : %s'%sklearn.__version__)
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import plotly
print('plotly: %s' % plotly.__version__)

pd.options.display.max_columns=50

df=pd.read_csv('weatherAUS.csv',encoding='utf-8')

df=df[pd.isnull(df['RainTomorrow'])==False]

df['RainTodayFlag']=df['RainToday'].apply(lambda x:1 if x== 'yes' else 0)
df['RainTomorrowFlag']=df['RainTomorrow'].apply(lambda x:1 if x== 'yes' else 0)

print(df)

x=df[['Humidity3pm']]
y=df['RainTomorrowFlag'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)