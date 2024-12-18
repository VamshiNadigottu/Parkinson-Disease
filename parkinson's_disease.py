# -*- coding: utf-8 -*-
"""Parkinson's disease

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uf5CDsjB0oxpCFHwTPSD5e1HrQ6cDq6_
"""

from google.colab import files

uploaded= files.upload()

# !pip install numpy

# !pip install xgboost

# !pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix,accuracy_score, classification_report

from xgboost import XGBClassifier

import os
for dirname, _, filenames in os.walk('../input/parkinsons-disease-data-set'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Read the data
df=pd.read_csv('parkinsons.data')
print(df.shape,'\n')
df.head()

df.describe()

df.info()

df.shape

df['status'].value_counts().plot(kind='pie', autopct = "%1.0f%%")

X_un=df.copy()
X_un=X_un.drop(['name','status'],axis=1)
y_un=df[['status']]

from sklearn.model_selection import StratifiedShuffleSplit
split=StratifiedShuffleSplit(n_splits=3,test_size=0.2,random_state=24)

for train_index,test_index in split.split(X_un,y_un):
    strat_train_set_x,strat_train_y=X_un.loc[train_index],y_un.loc[train_index]
    strat_test_set_x,strat_test_y=X_un.loc[test_index],y_un.loc[test_index]

print(strat_train_set_x.shape,strat_train_y.shape)
print(strat_test_set_x.shape,strat_test_y.shape)

#Train the model
from sklearn.metrics import precision_score, accuracy_score,recall_score
model=XGBClassifier(use_label_encoder=False,eval_metric='rmse')
model.fit(strat_train_set_x,strat_train_y)
y_pred=model.predict(strat_test_set_x)

print('accuracy score %.2f'% accuracy_score(y_pred,strat_test_y))
print('recall score %.2f'%recall_score(y_pred,strat_test_y))

print("Confusion Matrix: ")
cf_matrix=confusion_matrix(y_pred,strat_test_y)

print("\nClassification Report:")
print(classification_report(y_pred,strat_test_y))

confusion_matrix(y_pred, strat_test_y)

matrix = confusion_matrix(y_pred, strat_test_y)
matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]

#Build the plot
plt.figure(figsize=(16,7))

sns.set(font_scale=1.4)

sns.heatmap(matrix, annot=True, annot_kws={'size':10}, cmap=plt.cm.Greens, linewidths=0.2)

#Add Labels to the plot

class_names = ['False', 'True']
tick_marks = np.arange(len(class_names))

tick_marks2 = tick_marks + 0.5
plt.xticks(tick_marks, class_names, rotation=25)

plt.yticks(tick_marks2, class_names, rotation=0)
plt.xlabel('Predicted label')

plt.ylabel('True label')
plt.title('Confusion Matrix for XGBOOST Model')

plt.show()

input_data=(116.68200,131.11100,111.55500,0.01050,0.00009,0.00544,0.00781,0.01633,0.05233,0.48200,0.02757,0.03858,0.03590,0.08270,0.01309,20.65100,0.429895,0.825288,-4.443179,0.311173,2.342259,0.332634)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction==0):
  print("person doesnot have parkinson disease")
else:
   print("person has parkinson disease")

input_data=(88.33300,112.24000,84.07200,0.00505,0.00006,0.00254,0.00330,0.00763,0.02143,0.19700,0.01079,0.01342,0.01892,0.03237,0.01166,21.11800,0.611137,0.776156,-5.249770,0.391002,2.407313,0.249740)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction==0):
  print("person doesnot have parkinson disease")
else:
   print("person has parkinson disease")

input_data=(245.51000,262.09000,231.84800,0.00235,0.000010,0.00127,0.00148,0.00380,0.01608,0.14100,0.00906,0.00977,0.01149,0.02719,0.00476,24.60200,0.467489,0.631653,-7.156076,0.127642,2.392122,0.097336)

input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction==0):
  print("person doesnot have parkinson disease")
else:
   print("person has parkinson disease")

input_data=(252.45500,261.48700,182.78600,0.00185,0.000007,0.00092,0.00113,0.00276,0.01152,0.10300,0.00614,0.00730,0.00860,0.01841,0.00432,26.80500,0.610367,0.635204,-7.319510,0.200873,2.028612,0.086398)

prediction=model.predict(input_data_reshaped)
print(prediction)
if(prediction==0):
  print("person doesnot have parkinson disease")
else:
   print("person has parkinson disease")