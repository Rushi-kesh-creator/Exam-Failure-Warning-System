import pandas as pd
import random
data = []
for _ in range(1000):
    attendance = random.randint(40, 100)
    assignment1 = random.randint(0, 6)
    assignment2 = random.randint(0, 6)
    mid1 = random.randint(0, 24)
    mid2 = random.randint(0, 24)
    cgpa = round(random.uniform(4.0, 10.0), 2)
    # Pass/Fail Logic
    total_score = (
        attendance * 0.2 +
        assignment1 * 2 +
        assignment2 * 2 +
        mid1 * 1.5 +
        mid2 * 1.5 +
        cgpa * 4
    )
    result = 1 if total_score >= 80 else 0
    data.append([attendance,assignment1,assignment2,mid1,mid2,cgpa,result])
df = pd.DataFrame(data,columns=["attendance","assignment1","assignment2","mid1","mid2","cgpa","pass"])
df.to_csv("student_dataset.csv", index=False)
print("Dataset generated successfully!")