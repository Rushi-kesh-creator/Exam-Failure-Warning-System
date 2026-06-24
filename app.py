from flask import Flask
from models import User, Student, Subject, StudentSubject, Prediction
from extensions import db, login_manager, bcrypt
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

from routes import *
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)