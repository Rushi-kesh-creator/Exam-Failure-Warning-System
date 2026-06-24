import joblib
import pandas as pd

model = joblib.load("student_failure_model.pkl")

sample_student = pd.DataFrame([{
    "attendance": 85,
    "assignment1": 5,
    "assignment2": 4,
    "mid1": 18,
    "mid2": 20,
    "cgpa": 8.2
}])

prediction = model.predict(sample_student)

if prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")