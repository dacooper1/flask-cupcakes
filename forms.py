from wtforms import SelectField, StringField, IntegerRangeField, URLField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from models import DEFAULT_IMG

class NewCupcake(FlaskForm):
    flavor = StringField("First Name", validators=[InputRequired()])

    size = SelectField("First Name", validators=[InputRequired()], choices=[('small', 'small', ('medium', 'medium'), ('large', 'large'))])

    rating = IntegerRangeField("Rating", default=[1,5],validators=[InputRequired()])

    image = URLField("Image URL", default=DEFAULT_IMG)