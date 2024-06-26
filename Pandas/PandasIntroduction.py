import pandas as pd
import numpy as np

#Crear DataFrame

data = np.array([['','Col1','Col2'], ['Fila1',11, 22], ['Fila2', '33', '34']])
print(pd.DataFrame(data = data[1:, 1:], index= data[1:, 0], columns= data[0, 1:]))

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("DataFrame: ")
print(df)
#data frame shape
print("Shape: ")
print('  ',df.shape)
#DateFrmae Height
print()
print("Height: ",len(df.index))
#Datafrema statistics
print()
print("Datafrema statistics: ")
print(df.describe())

#Datafreme meansurement
print()
print("Datafreme meansurement: ")
print(df.mean())
#Datafreme correlation
print()
print("Datafreme correlation: ")
print(df.corr())









print()
#Serie
series = pd.Series({"Colombia": "Bogota", "Argentina": "Buenos Aires", "Perú": "Lima"})
print("Serie: ")
print(series)
