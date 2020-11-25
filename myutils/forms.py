from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField,TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError



class CustomForm(FlaskForm):
	link = StringField('Link')
	para = TextAreaField('para')
	no_of_sent=StringField('no_of_sent')
	no_min_words_per_sent=StringField('no_min_words_per_sent')

	submit = SubmitField('summarize')




