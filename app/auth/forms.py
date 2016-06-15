from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField, BooleanField, DecimalField, FileField, TextAreaField
from wtforms.validators import data_required


class AddProduct(Form):
    name = StringField('Product Name', validators=[data_required()], description="Product Name")
    description = TextAreaField("Product Description", description='Product Description')
    image = FileField('Image Field')
    cost = DecimalField('Price', places=2, description="000.00")
    active = BooleanField('Active')
