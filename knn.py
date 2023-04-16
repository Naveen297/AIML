import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sn

# Load the IRIS dataset
iris = load_iris()

# Convert dataset into a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['flowername'] = df.target.apply(lambda x: iris.target_names[x])

# Split the dataset into features/inputs (X) and target variable (y)
X = df.drop(['target', 'flowername'], axis=1)
y = df.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a K-Nearest Neighbors classifier with a specified value of k
k = 3  # Example value of k
knn = KNeighborsClassifier(n_neighbors=k)

# Train the model
knn.fit(X_train, y_train)

# Predict the target variable on the testing data
y_pred = knn.predict(X_test)

# Calculate accuracy, confusion matrix, and classification report
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

# Print the results
print("Accuracy of K-Nearest Neighbors classifier: {:.2f}%".format(accuracy * 100))
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", classification_report)

# Create a heatmap for the confusion matrix
plt.figure(figsize=(7, 5))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
