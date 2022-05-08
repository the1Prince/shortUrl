from logging import PlaceHolder
from pydoc import classname
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ShortenForm(FlaskForm):
    inlineFormInputGroupUsername2=StringField('Shorten')
    submit=SubmitField('Generate short URL')