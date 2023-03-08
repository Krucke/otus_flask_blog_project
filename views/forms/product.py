from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        'nameqwe', 
        validators=[
            DataRequired(),
            Length(min=3),
        ])
