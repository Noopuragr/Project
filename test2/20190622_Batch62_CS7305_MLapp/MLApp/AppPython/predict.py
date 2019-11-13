# Import libraries
import os
from joblib import load
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score

PATH = os.getcwd()

clf = load(PATH + '/pickle/model.pkl')

data = pd.read_csv(PATH+"/data/test_cases.csv")
print(data)
y = data['y']

data.drop('y', axis=1, inplace=True)

y_pred = clf.predict(data)

data["y_pred"] = y_pred

print(data.columns)

data.columns

print(data.head())
print("Accuracy = ", accuracy_score(y, y_pred))
print("Recall   = ", recall_score(y, y_pred, pos_label='yes'))