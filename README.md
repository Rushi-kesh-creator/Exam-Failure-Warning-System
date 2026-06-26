# 🎓 AI-Based Exam Failure Early Warning System :-
An AI-powered web application that helps educational institutions identify students who are at risk of failing examinations at an early stage. The system enables faculty members to manage student records, enter academic performance data, and leverage a Machine Learning model to predict whether a student is likely to **PASS** or **FAIL**.
The application is developed using **Flask** for the backend, **PostgreSQL (Supabase)** as the cloud database, **SQLAlchemy** as the ORM, **Bootstrap** for the responsive user interface, and a **Random Forest Classifier** built with **Scikit-learn** for predictive analytics.
The prediction model analyzes each student's academic performance based on:
* **Internal Marks** (80% of the higher mid examination + 20% of the lower mid examination + Assignment Marks)
* **Attendance Percentage**
* **CGPA**
Based on these inputs, the system predicts whether the student is likely to **PASS** or **FAIL**, allowing faculty to identify at-risk students early and provide timely academic support.

## ✨ Features
* 🔐 Secure Faculty Registration and Login Authentication
* 👨‍🎓 Add, View, Update, and Delete Student Records
* 📚 Manage Student Subject Information
* 📝 Enter Student Academic Performance Data
* 🤖 AI-based PASS/FAIL Prediction using a Random Forest Machine Learning model
* 📊 Prediction based on Internal Marks, Attendance, and CGPA
* 💾 Store Prediction Results in a PostgreSQL (Supabase) Database
* 📜 View Prediction History
* ⚠️ Identify Students at Risk of Failure
* 📈 Faculty Dashboard with Student Management
* 🎨 Responsive and User-Friendly Interface using Bootstrap
* ☁️ Cloud Database Integration with Supabase
* 🔒 Session Management using Flask-Login

## 🛠️ Tech Stack
### Backend
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-WTF
### Database
* PostgreSQL (Supabase)
### Frontend
* HTML5
* CSS3
* Bootstrap 5
* Jinja2 Templates
### Machine Learning
* Scikit-learn
* Random Forest Classifier
* Pandas
* NumPy
* Joblib
### Development Tools
* Python 3.x
* Visual Studio Code

## 📁 Project Structure
ExamFailureWarningSystem/
│
├── static/                     # CSS, JavaScript, Images
├── templates/                  # HTML Templates
│
├── app.py                      # Application Entry Point
├── models.py                   # Database Models
├── routes.py                   # Application Routes
├── forms.py                    # Flask-WTF Forms
├── extensions.py               # Database & Login Manager
├── train_model.py              # Machine Learning Model Training
├── student_failure_model.pkl   # Trained Random Forest Model
├── requirements.txt            # Project Dependencies
├── README.md                   # Project Documentation
│
└── instance/

## 🚀 Installation & Setup
Follow these steps to run the project locally.
### 1. Clone the Repository
bash
git clone https://github.com/<your-username>/ExamFailureWarningSystem.git
### 2. Navigate to the Project Directory
bash
cd ExamFailureWarningSystem
### 3. Create a Virtual Environment
**Windows**
bash
python -m venv venv
### 4. Activate the Virtual Environment
**Windows (Command Prompt)**
bash
venv\Scripts\activate

**Windows (PowerShell)**
powershell
venv\Scripts\Activate.ps1
### 5. Install Dependencies
pip install -r requirements.txt
### 6. Configure Environment Variables
Create a `.env` file in the project root and add the following:
env
SECRET_KEY=your_secret_key
DATABASE_URL=your_supabase_postgresql_connection_string
### 7. Run the Application
python app.py
Open your browser and visit:
http://127.0.0.1:5000

## 📖 Usage
1. Register as a faculty member.
2. Log in using your faculty credentials.
3. Add student details.
4. Add subject information for each student.
5. Enter academic details including:

   * Mid Examination Marks
   * Assignment Marks
   * Attendance Percentage
   * CGPA
6. Submit the form to generate a PASS/FAIL prediction.
7. View the prediction history.
8. Identify students who are at risk of failing and provide academic guidance.

## 🧠 Machine Learning Model
The prediction module is powered by a **Random Forest Classifier** developed using **Scikit-learn**.
### Input Features
The model uses the following student performance indicators:
* **Internal Marks**
  * 80% of the Higher Mid Examination Marks
  * 20% of the Lower Mid Examination Marks
  * Assignment Marks
* **Attendance Percentage**
* **CGPA**
### Prediction
Based on these academic parameters, the model predicts whether a student is likely to:
* ✅ PASS
* ❌ FAIL
The trained model is stored as:
student_failure_model.pkl
The Flask application loads this model using **Joblib** and performs real-time predictions whenever faculty members submit student academic data.

## 🔮 Future Enhancements
* Email notifications for students identified as at risk.
* Data visualization dashboards using interactive charts.
* Integration with Learning Management Systems (LMS).
* Support for multiple machine learning algorithms and performance comparison.
* Student portal to view academic progress and predictions.
* Export prediction reports as PDF or Excel.
* Improved analytics for faculty and administrators.
* **Previous Question Paper Analysis:** Allow faculty to upload previous years' question papers and use AI/NLP techniques to identify frequently asked and important topics. Based on a student's predicted risk level, the system can recommend important questions and topics for focused exam preparation.

## 👨‍💻 Author
**Sai RushiKesh Reddy Onteddu**
* 🎓 B.Tech Student
* 💡 Interested in Artificial Intelligence, Machine Learning, and Full-Stack Development
* 📧 Email:rushikeshonteddu06@gmail.com
* 💼 LinkedIn: https://linkedin.com/in/www.linkedin.com/in/onteddu-sai-rushikesh-reddy-393a16318
* 🐙 GitHub: https://github.com/Rushi-kesh-creator



