import joblib
import pandas as pd
import csv
from app import app
from flask import render_template, redirect, url_for, flash,request,Response
from flask_login import login_user, logout_user, login_required, current_user
from forms import FacultyRegistrationForm,LoginForm,StudentForm,SubjectForm,AddSubjectForm,EditStudentForm,EditSubjectForm
from models import User, Student, StudentSubject,Subject,Prediction
from extensions import db

model = joblib.load("ml/student_failure_model.pkl")
@app.route("/")
@app.route("/home")
def home_page():
    return  render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = FacultyRegistrationForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email=form.email.data,role="faculty")
        user_to_create.password = form.password1.data
        db.session.add(user_to_create)
        db.session.commit()
        flash("Faculty account created successfully!")
        return redirect(url_for("home_page"))
    return render_template("register.html",form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}',category='success')
            return redirect(url_for('faculty_dashboard'))
        else:
            flash('Username and password do not match',category='danger')
    return render_template('login.html',form=form)

@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash("You have been logged out!",category='info')
    return redirect(url_for('home_page'))

@app.route('/faculty/dashboard')
@login_required
def faculty_dashboard():
    total_students = Student.query.count()
    total_subjects = Subject.query.count()
    total_predictions = Prediction.query.count()
    high_risk_students = Prediction.query.filter_by(risk_level='HIGH').count()
    recent_predictions = Prediction.query.order_by(Prediction.created_at.desc()).limit(5).all()
    pass_count = Prediction.query.filter_by(predicted_result='PASS').count()
    fail_count = Prediction.query.filter_by(predicted_result='FAIL').count()
    return render_template(
        'faculty_dashboard.html',
        total_students=total_students,
        total_subjects=total_subjects,
        total_predictions=total_predictions,
        high_risk_students=high_risk_students,
        recent_predictions=recent_predictions,
        pass_count=pass_count,
        fail_count=fail_count
    )

@app.route('/student/create', methods=['GET', 'POST'])
@login_required
def create_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(roll_no=form.roll_no.data,name=form.name.data, branch=form.branch.data,year=form.year.data,section=form.section.data,cgpa=form.cgpa.data)
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully!",category="success")
        return redirect(url_for('faculty_dashboard'))
    return render_template('create_student.html',form=form)
@app.route('/students')
@login_required
def students_page():
    search = request.args.get('search')
    if search:
        students = Student.query.filter(Student.name.ilike(f'%{search}%')).all()
    else:
        students = Student.query.all()
    return render_template('students.html',students=students)
@app.route('/add-subject', methods=['GET', 'POST'])
@login_required
def add_subject():
    form = SubjectForm()
    form.student_id.choices = [ (s.id, f"{s.roll_no} - {s.name}") for s in Student.query.all()]
    form.subject_id.choices = [ (s.id, s.subject_name) for s in Subject.query.all()]
    if form.validate_on_submit():
        subject = StudentSubject(student_id=form.student_id.data,subject_id=form.subject_id.data,
            attendance=form.attendance.data,
            assignment1=form.assignment1.data,
            assignment2=form.assignment2.data,
            mid1=form.mid1.data,
            mid2=form.mid2.data)
        db.session.add(subject)
        db.session.commit()
        flash("Subject data added successfully!", "success")
        return redirect(url_for('faculty_dashboard'))
    return render_template('add_subject.html', form=form)
@app.route('/subject/create', methods=['GET', 'POST'])
@login_required
def create_subject():
    form = AddSubjectForm()
    if form.validate_on_submit():
        subject = Subject(subject_name=form.subject_name.data)
        db.session.add(subject)
        db.session.commit()
        flash("Subject added successfully!", "success")
        return redirect(url_for('faculty_dashboard'))
    return render_template('create_subject.html',form=form)

@app.route('/subject-records')
@login_required
def subject_records():
    records = StudentSubject.query.all()
    return render_template('subject_records.html',records=records)

@app.route('/predict/<int:record_id>')
@login_required
def predict_student(record_id):
    record = StudentSubject.query.get_or_404(record_id)
    student = Student.query.get(record.student_id)
    higher_mid = max(record.mid1, record.mid2)
    lower_mid = min(record.mid1, record.mid2)
    internal_marks = round(
        record.assignment1 +
        record.assignment2 +
        (0.8 * higher_mid) +
        (0.2 * lower_mid)
    )
    features = pd.DataFrame([{
        "internal_marks": internal_marks,
        "attendance": record.attendance,
        "cgpa": student.cgpa
    }])
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    confidence = float(round(max(probabilities) * 100, 2))
    result = "PASS" if prediction == 1 else "FAIL"
    risk_score =confidence / 100
    risk_level = "HIGH" if result == "FAIL" else "LOW"
    new_prediction = Prediction(
        student_id=record.student_id,
        subject_id=record.subject_id,
        risk_score=risk_score,
        risk_level=risk_level,
        predicted_result=result,
        confidence=confidence)
    db.session.add(new_prediction)
    db.session.commit()
    flash(f"Prediction Result: {result} ({risk_level} RISK)","success")
    return redirect(url_for('subject_records'))

@app.route('/predictions')
@login_required
def predictions_page():
    predictions = Prediction.query.all()
    return render_template('predictions.html',predictions=predictions)

@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = EditStudentForm(obj=student)
    if form.validate_on_submit():
        student.roll_no = form.roll_no.data
        student.name = form.name.data
        student.branch = form.branch.data
        student.year = form.year.data
        student.section = form.section.data
        student.cgpa = form.cgpa.data
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('students_page'))
    return render_template('edit_student.html',form=form)

@app.route('/delete_student/<int:student_id>')
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    Prediction.query.filter_by(student_id=student.id).delete()
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('students_page'))


@app.route('/edit_record/<int:record_id>', methods=['GET', 'POST'])
@login_required
def edit_record(record_id):
    record = StudentSubject.query.get_or_404(record_id)
    form = EditSubjectForm(obj=record)
    if form.validate_on_submit():
        record.attendance = form.attendance.data
        record.assignment1 = form.assignment1.data
        record.assignment2 = form.assignment2.data
        record.mid1 = form.mid1.data
        record.mid2 = form.mid2.data
        db.session.commit()
        flash('Subject record updated successfully!', 'success')
        return redirect(url_for('subject_records'))
    return render_template('edit_record.html',form=form)

@app.route('/delete_record/<int:record_id>')
@login_required
def delete_record(record_id):
    record = StudentSubject.query.get_or_404(record_id)
    Prediction.query.filter_by(
        student_id=record.student_id,
        subject_id=record.subject_id
    ).delete()
    db.session.delete(record)
    db.session.commit()
    flash('Subject record deleted successfully!', 'success')
    return redirect(url_for('subject_records'))

@app.route('/high-risk-students')
@login_required
def high_risk_students():
    predictions = Prediction.query.filter_by(risk_level='HIGH').all()
    return render_template('high_risk_students.html',predictions=predictions)

@app.route('/analytics')
@login_required
def analytics():
    pass_count = Prediction.query.filter_by(predicted_result='PASS').count()
    fail_count = Prediction.query.filter_by(predicted_result='FAIL').count()
    return render_template('analytics.html',pass_count=pass_count,fail_count=fail_count)

@app.route('/export_predictions')
@login_required
def export_predictions():
    predictions = Prediction.query.all()
    print("Total Predictions:", len(predictions))
    csv_data = "Student,Subject,Risk Level,Result,Confidence\n"
    for p in predictions:
        csv_data += (
            f"{p.student.name},"
            f"{p.subject.subject_name},"
            f"{p.risk_level},"
            f"{p.predicted_result},"
            f"{p.confidence}%\n"
        )
    return Response(
        csv_data,
        mimetype='text/csv',
        headers={'Content-Disposition':'attachment; filename=predictions.csv'})
