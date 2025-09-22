# Import the modules needed

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model as L  # SciKit learn is "sklearn"

# Download and Prepare the Data
data_root = "https://raw.githubusercontent.com/ageron/data/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# Visualize the Data
lifesat.plot(kind="scatter", grid=True,
              x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# Select a linear Model
model = L.LinearRegression()

# Train the Model
model.fit(X, y)

# Make a Prediction for Cyprus
X_new = [[37_665.2]] # Cyprus' GDP per capita in 2020
print(model.predict(X_new)) # Output : [[6.30165767]]

print("Hi")