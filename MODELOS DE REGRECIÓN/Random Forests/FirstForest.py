import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

california_housing = fetch_california_housing()

df = pd.DataFrame(california_housing.data, columns= california_housing.feature_names)
df['PRICE'] = california_housing.target

x_frt = df['AveRooms'].values.reshape(-1,1)
y_frt = df['PRICE'].values.reshape(-1,1)


#Slipt data
x_train, x_test, y_train, y_test = train_test_split(x_frt, y_frt, test_size=0.3, random_state=42)

#Train model
frt = RandomForestRegressor(n_estimators = 1000, max_depth = 50)
frt.fit(x_train, y_train)

#Prediction
y_pred = frt.predict(x_test)

#Model Accuracy
print('Model Accuracy')
print(frt.score(x_train,y_train))

#Sow data
x_grid = np.arange(min(x_test), max(x_test), 0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(x_test, y_test)
plt.plot(x_grid, frt.predict(x_grid), color ='r')
plt.show()

