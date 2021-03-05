from django import forms

from webapp.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'remainder', 'price')


class ProductDeleteForm(forms.Form):
    name = forms.TimeField(required=True, label='Enter of the name, to delete! ')