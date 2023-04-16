import numpy as np
import matplotlib.pyplot as plt

# Define the input data
X = np.array([1, 2, 3, 4, 5]) # Input feature
y = np.array([2, 4, 6, 8, 10]) # Target variable

# Plot the input data
plt.scatter(X, y, color='red', marker='+')
plt.xlabel('Input Feature (X)')
plt.ylabel('Target Variable (y)')
plt.title('Linear Regression - Single Variable')
plt.show()

# Implement linear regression
m, c = np.polyfit(X, y, deg=1) # Fit a first-degree polynomial (line) to the data
predicted_y = m * X + c # Predicted values of y using the fitted line

# Plot the fitted line and predicted values
plt.scatter(X, y, color='red', marker='+')
plt.plot(X, predicted_y, color='blue')
plt.xlabel('Input Feature (X)')
plt.ylabel('Target Variable (y)')
plt.title('Linear Regression - Single Variable')
plt.show()

# Print the slope (m) and y-intercept (c) of the fitted line
print('Slope (m):', m)
print('Y-intercept (c):', c)

# Use the fitted line to make predictions
new_X = np.array([6, 7, 8]) # New input feature values for prediction
predicted_new_y = m * new_X + c # Predicted values of y for the new input feature values
print('Predicted values for new X:', predicted_new_y)
