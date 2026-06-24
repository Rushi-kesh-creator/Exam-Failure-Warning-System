from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField,FloatField,SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email
class FacultyRegistrationForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email',validators=[DataRequired(),Email()])
    password1 = PasswordField(label='Password',validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1')])
    submit = SubmitField(label='Register')
class LoginForm(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    submit = SubmitField(label='Login')
class StudentForm(FlaskForm):
    roll_no = StringField(label='Roll Number',validators=[DataRequired()])
    name = StringField(label='Student Name',validators=[DataRequired()])
    branch = StringField(label='Branch',validators=[DataRequired()])
    year = IntegerField(label='Year',validators=[DataRequired()])
    section = StringField(label='Section',validators=[DataRequired()])
    cgpa = FloatField(label='CGPA',validators=[DataRequired()])
    submit = SubmitField(label='Add Student')
class SubjectForm(FlaskForm):
    student_id = SelectField('Student', coerce=int, validators=[DataRequired()])
    subject_id = SelectField('Subject', coerce=int, validators=[DataRequired()])
    attendance = FloatField('Attendance', validators=[DataRequired()])
    assignment1 = FloatField('assignment1', validators=[DataRequired()])
    assignment2 = FloatField('assignment2', validators=[DataRequired()])
    mid1 = FloatField('mid1', validators=[DataRequired()])
    mid2 = FloatField('mid2', validators=[DataRequired()])
    submit = SubmitField('Save')
class AddSubjectForm(FlaskForm):
    subject_name = StringField('Subject Name',validators=[DataRequired()])
    submit = SubmitField('Add Subject')

class EditStudentForm(FlaskForm):
    roll_no = StringField(label='Roll Number',validators=[DataRequired()])
    name = StringField(label='Student Name',validators=[DataRequired()])
    branch = StringField(label='Branch',validators=[DataRequired()])
    year = StringField(label='Year',validators=[DataRequired()])
    section = StringField(label='Section',validators=[DataRequired()])
    cgpa = StringField(label='CGPA')
    submit = SubmitField(label='Update Student')
class EditSubjectForm(FlaskForm):
    attendance = FloatField('Attendance',validators=[DataRequired()])
    assignment1 = FloatField('Assignment1',validators=[DataRequired()])
    assignment2 = FloatField('Assignment2',validators=[DataRequired()])
    mid1 = FloatField('Mid1',validators=[DataRequired()])
    mid2 = FloatField('Mid2',validators=[DataRequired()])
    submit = SubmitField('Update Record')
