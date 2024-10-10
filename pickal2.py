# importing required libraries
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("D:/Brain Stroke Analysis_Project/New_brain_stroke.csv")

data = df.copy()


data['gender'] = data['gender'].map({'Female':1,'Male':0})
data['ever_married'] = data['ever_married'].map({'Yes': 1, 'No': 0})
data['work_type'] = data['work_type'].map({'Private': 0, 'Self-employed': 1, 'Govt_job':2, 'children':3})
data['Residence_type'] = data['Residence_type'].map({'Urban': 1, 'Rural':0})
data['smoking_status'] = data['smoking_status'].map({'formerly smoked':0, 'never smoked':1, 'smokes':2, 'Unknown':3})

    
X = data.iloc[:,:-1]
y = data['stroke']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

model = RandomForestClassifier(n_estimators = 100,criterion = 'gini',max_depth= None,min_samples_split=2, max_features='sqrt',min_impurity_decrease=0.0, bootstrap=True,ccp_alpha=0.0)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)

p = model.score(X_test,y_test)
print(p)

print('Classification Report\n', classification_report(y_test, y_pred))
print('Accuracy: {}%\n'.format(round((accuracy_score(y_test, y_pred)*100),2)))

cm = confusion_matrix(y_test, y_pred)
print(cm)

filename = 'RandomForestClassifier-model5.pkl'
pickle.dump(model, open(filename, 'wb'))