import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate synthetic test data
np.random.seed(42)
X = np.random.rand(100, 3) * 10 # Three input features
y = 2 * X[:, 0] + 3 * X[:, 1] + 4 * X[:, 2] + np.random.randn(100) * 0.5 # Target variable with noise

# Create a linear regression model and fit it to the data
reg = LinearRegression()
reg.fit(X, y)

# Print the coefficients (slope) and y-intercept of the fitted line
print('Coefficients (Slope):', reg.coef_)
print('Y-intercept (Intercept):', reg.intercept_)

# Use the trained model to make predictions on new data
new_data = np.array([[3, 4, 5], [2, 1, 6]]) # New input feature values for prediction
predicted_y = reg.predict(new_data) # Predicted values of y for the new input feature values
print('Predicted values for new data:', predicted_y)

# Plot the predicted values
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, color='b', label='Actual Data') # Scatter plot of actual data
plt.scatter(new_data[:, 0], predicted_y, color='r', label='Predicted Data') # Scatter plot of predicted data
plt.xlabel('X1')
plt.ylabel('y')
plt.legend()
plt.show()
