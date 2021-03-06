from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('articles title',validators=[Required()])
    review = TextAreaField('news review', validators=[Required()])
    submit = SubmitField('Submit')