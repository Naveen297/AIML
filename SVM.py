import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load digits dataset
digits = load_digits()

# Create dataframe from dataset
df = pd.DataFrame(digits.data, digits.target)
df['target'] = digits.target

# Check for null values in dataframe
if df.isna().any().any():
    df.fillna(df.mean(), inplace=True)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis=1), df.target, test_size=0.3)

# Create SVM model with RBF kernel
rbf_model = SVC(kernel='rbf')

# Train SVM model
rbf_model.fit(X_train, y_train)

# Check performance score of SVM model
rbf_score = rbf_model.score(X_test, y_test)
print("Accuracy of RBF kernel SVM model: ", rbf_score)
