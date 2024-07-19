from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score, accuracy_score


breast_cancer = load_breast_cancer()

x = breast_cancer.data
y = breast_cancer.target


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#Scale the data because it is different and needs to be the same
escalar = StandardScaler()
x_train = escalar.fit_transform(x_train)
x_test = escalar.transform(x_test)

#Build the model
logic = LogisticRegression()
logic.fit(x_train, y_train)

#Prediction
y_pred = logic.predict(x_test)

#Model performance
matrix = confusion_matrix(y_test, y_pred)
print(f'The confusion matriz is: \n{matrix}\n')

#Sensitivity
recall = recall_score(y_test, y_pred)
print(f'The recall is: \n{recall}\n')

#Precision
precision = precision_score(y_pred, y_test)
print(f'The precision is : \n{precision}\n')

#Accurancy
accurancy = accuracy_score(y_pred, y_test)
print(f'The accurrancy is : \n{accurancy}\n')

#F1
f1 = f1_score(y_pred, y_test)
print(f'The f1 is: \n{f1}')