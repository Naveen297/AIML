import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import graphviz

# Read the dataset from the given URL
url = 'https://raw.githubusercontent.com/codebasics/py/master/ML/9_decision_tree/salaries.csv'
df = pd.read_csv(url)

# Drop 'salary_more_then_100k' column
inputs = df.drop('salary_more_then_100k', axis=1)

# Store the target variable in a separate variable
target = df['salary_more_then_100k']

# Label encoding for categorical columns
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])
inputs_n = inputs.drop(['company', 'job', 'degree'], axis=1)

# Implement Decision Tree
model = tree.DecisionTreeClassifier()

# Fit/train the model
model.fit(inputs_n, target)

# Analyze the performance of the model
score = model.score(inputs_n, target)
print("Accuracy of Decision Tree model: ", score)

# Generate visual representation of Decision Tree
dot_data = tree.export_graphviz(model,
                                feature_names=inputs_n.columns,
                                class_names=target.unique(),
                                filled=True)
graph = graphviz.Source(dot_data)
graph.render(filename='decision_tree', format='png', cleanup=True)

# Open the generated image file
graph.view()
