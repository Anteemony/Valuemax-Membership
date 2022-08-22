from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2,max=20)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  phone = StringField(validators=[DataRequired()])
  submit = SubmitField("Add Member")

class LoginForm(FlaskForm):
  phone = StringField(validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Add Member")