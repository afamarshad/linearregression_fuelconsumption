import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Making data frame
df = pd.read_csv("FuelConsumption.csv")
df.head()

# Selecting x as engine size as independent and y as Co2Emissions as dependent variable
X = df[["ENGINESIZE"]]
y = df["CO2EMISSIONS"]

# Fitting the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predicts a single value based on input
new_enginesize = [[2.6]]
prediction = model.predict(new_enginesize)

print("\nPredicted CO2 Emissions:")
print(prediction[0])


# Predict a range of values using np.linspace for plotting the regression line
# Create prediction line
x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model.predict(x_line)


# Plot regression line
plt.plot(x_line, y_line, color="red", label="Best Fit Line")
plt.scatter(X, y, color="blue", label="Data Points")

# Labels and styling
plt.xlabel("ENGINESIZE")
plt.ylabel("CO2 EMISSIONS")
plt.title("Linear Regression: Engine Size vs CO2 Emissions")
plt.legend()
plt.grid()
plt.show()

