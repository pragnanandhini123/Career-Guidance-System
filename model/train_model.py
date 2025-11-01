import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.DataFrame({
    'marks': [80, 60, 90, 70, 85, 50],
    'skills': [8, 5, 9, 6, 8, 4],
    'interest': [7, 6, 9, 5, 8, 3],
    'career_path': ['Data Science', 'Networking', 'AI', 'Web Development', 'Data Science', 'Embedded']
})

X = data[['marks', 'skills', 'interest']]
y = data['career_path']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open('model/career_model.pkl', 'wb'))
print("✅ Model trained and saved successfully.")
