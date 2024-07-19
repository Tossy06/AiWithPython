from sklearn.datasets import  load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix    

breast_cancer = load_breast_cancer()
x = breast_cancer.data
y = breast_cancer.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5, metric= 'minkowski', p = 2)
knn.fit(x_train, y_train)

y_pred = knn.predict(x_test)

matix = confusion_matrix(y_pred, y_test)
print(f'The confusion matrix is: \n{matix}')