from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, recall_score, precision_score, f1_score, accuracy_score

breast_cancer = load_breast_cancer()

x = breast_cancer.data
y = breast_cancer.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

frt = RandomForestClassifier(n_estimators=4, max_depth= 4)
frt.fit(x_train, y_train)

y_pred = frt.predict(x_test)


matrix = confusion_matrix(y_pred, y_test)
print(f'The confusion matriz is: \n{matrix}\n')