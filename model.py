import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data = pd.read_excel("~/Downloads/XTern 2024 Artificial Intelegence Data Set.xlsx")

#Updates the Year column to only contain integer values
year_mapping = {'Year 1': '1', 'Year 2': '2', 'Year 3': '3', 'Year 4': '4'}
for idx, value in enumerate(data['Year']):
    if value in year_mapping:
        data.at[idx, 'Year'] = year_mapping[value]


X = data['Year']  # Features
y = data['Order']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = X_train.values.reshape(-1, 1)  # Convert to a 2D array
X_test = X_test.values.reshape(-1, 1)  # Convert to a 2D array


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)
