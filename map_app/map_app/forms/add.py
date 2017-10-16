from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class AddTourPoint(FlaskForm):
    """
    A form to add new users.
    Fields:
        address: The address of the establishment that the user wishes to add
        name: The name of the establishment
        category: Whether the establishment is a park, museum or restaurant
        public: Whether this location should be displayed publicly or for this user only
    """
    address = StringField('address', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    category = SelectField(
            'category',
            choices=[
                ('park', 'Park'),
                ('museum', 'Museum'),
                ('restaurant', 'Restaurant')
                ],
            validators=[DataRequired()])
    public = BooleanField('public', default=False)
