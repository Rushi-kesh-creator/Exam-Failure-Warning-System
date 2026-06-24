from extensions import db, bcrypt
from flask_login import UserMixin


# ---------------- USER ----------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    def __repr__(self):
        return f"User('{self.username}', '{self.role}')"


# ---------------- STUDENT ----------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(5), nullable=False)
    cgpa = db.Column(db.Float, nullable=True)
    # relation
    subjects = db.relationship('StudentSubject', backref='student', lazy=True, cascade='all, delete-orphan')
    def __repr__(self):
        return f"Student('{self.name}', '{self.roll_no}')"


# ---------------- SUBJECT ----------------
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(100), nullable=False)  # ❗ removed unique
    students = db.relationship('StudentSubject', backref='subject', lazy=True)
    def __repr__(self):
        return f"Subject('{self.subject_name}')"


# ---------------- STUDENT SUBJECT (ML CORE TABLE) ----------------
class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    attendance = db.Column(db.Float, nullable=False)
    assignment1 = db.Column(db.Float, nullable=False)
    assignment2 = db.Column(db.Float, nullable=False)
    mid1 = db.Column(db.Float, nullable=False)
    mid2 = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f"StudentSubject(Student={self.student_id}, Subject={self.subject_id})"


# ---------------- PREDICTION ----------------
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    risk_score = db.Column(db.Float, nullable=False)     # 0 to 1
    risk_level = db.Column(db.String(20), nullable=False) # LOW / MEDIUM / HIGH
    predicted_result = db.Column(db.String(10), nullable=True)  # PASS / FAIL
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    student = db.relationship('Student')
    subject = db.relationship('Subject')
    def __repr__(self):
        return f"Prediction('{self.risk_level}', {self.risk_score})"