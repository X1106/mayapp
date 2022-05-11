# models.py
from Flask import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import CheckConstraint

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def add_user(self):
        with db.session.begin(subtransactions=True):
            db.session.add(self)
        db.session.commit()
    
    @classmethod
    def select_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

class Member(db.Model):

    __tablename__ = 'members'
    __table_args__ = (
        CheckConstraint('update_at >= create_at'), 
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, server_default='noname')
    manager= db.Column(db.String(20), nullable=False)
    mail = db.Column(db.String(40), nullable=False, unique=True)
    comment = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)

    def __init__(self, name, manager, mail,comment,create_at,update_at ):
        self.name = name
        self.manager = manager
        self.mail = mail
        self.comment = comment
        self.create_at= create_at
        self.update_at  = update_at 


