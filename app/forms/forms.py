from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class NewsSearchForm(FlaskForm):

    newstitle = StringField('Search News',validators=[Required()])
    # review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')