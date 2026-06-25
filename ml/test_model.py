import joblib
import pandas as pd

model = joblib.load("student_failure_model.pkl")

internal_marks = (
    5 +
    4 +
    (0.8 * max(18,20)) +
    (0.2 * min(18,20))
)

sample_student = pd.DataFrame([{
    "internal_marks": internal_marks,
    "attendance": 85,
    "cgpa": 8.2
}])

prediction = model.predict(sample_student)

if prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")