import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Generate synthetic test data for binary classification
np.random.seed(42)
X = np.random.randn(100, 2) * 2 + np.array([5, 5]) # Input features
y = np.random.randint(0, 2, 100) # Binary target variable (0 or 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model and fit it to the training data
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Use the trained model to make predictions on the testing data
y_pred = logreg.predict(X_test)

# Calculate accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Generate classification report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# Plot the decision boundary
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Logistic Regression - Decision Boundary')
plt.show()
