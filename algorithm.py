import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv("Diabetes data.csv")
print(data)
x = data.drop('Outcome', axis=1)
print(x)
y = data['Outcome']
print(y)

Xtrain, Xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.3, random_state = 1)
print(Xtrain)
print(ytrain)
print(Xtest)
print(ytest)

model = DecisionTreeClassifier()
model.fit(Xtrain, ytrain)

predict = model.predict(Xtest)
print(accuracy_score(predict, ytest))

filename = 'model'
joblib.dump(model, filename)
