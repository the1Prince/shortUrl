from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    firstname = db.Column(db.String(64))
    lastname=db.Column(db.String(64))
    username=db.Column(db.String(64),unique=True)
    password=db.Column(db.String())
    email=db.Column(db.String(64),unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)