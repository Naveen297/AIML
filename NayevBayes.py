import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load Titanic dataset from URL
url = r'https://raw.githubusercontent.com/codebasics/py/master/ML/14_naive_bayes/titanic.csv'
titanic_df = pd.read_csv(url)

# Drop unnecessary columns
titanic_df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)

# Fill missing values in 'Age' column with mean
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)

# Convert 'Sex' column to numeric (0 for female, 1 for male)
titanic_df['Sex'] = titanic_df['Sex'].map({'female': 0, 'male': 1})

# Prepare input features and target variable
X = titanic_df[['Sex', 'Age', 'Fare']]
y = titanic_df['Survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Gaussian Naive Bayes model and fit it to the training data
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = gnb.predict(X_test)

# Calculate accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Predict the probability of survival for a few sample passengers
sample_passengers = [[0, 25, 50], [1, 30, 100], [0, 22, 20], [1, 35, 10]]
probabilities = gnb.predict_proba(sample_passengers)
for i in range(len(sample_passengers)):
    print("Probability of survival for passenger {}: {:.2f}%".format(sample_passengers[i], probabilities[i][1] * 100))
