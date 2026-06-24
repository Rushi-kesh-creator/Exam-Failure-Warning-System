import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
df = pd.read_csv("student_dataset.csv")
X = df[["attendance","assignment1","assignment2","mid1","mid2","cgpa"]]
y = df["pass"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
joblib.dump(model, "student_failure_model.pkl")
print("Model saved successfully!")