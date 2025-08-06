from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import InputRequired,Length
class LoginForm(FlaskForm):
    username=StringField('Username',validators=[InputRequired()])
    password=PasswordField('Password',validators=[InputRequired(),Length(min=6)])
    submit=SubmitField('Login')
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Register')