# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask import Flask

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SECRET_KEY'] = 'your_secret_key'
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"

# # Run this in terminal to create the database:
# # >>> from models import db, app
# # >>> with app.app_context():
# # >>>     db.create_all()
