import pandas as pd
data_set = pd.read_csv("diabetes.csv")
x = data_set.iloc[:, 0:8].values
y = data_set.iloc[:, -1].values

from sklearn.model_selection import train_test_solit
