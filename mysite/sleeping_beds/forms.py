from django import forms
from django.contrib.auth.models import User
from .models import Customers, Products, Home_page_images

class Update_Customer_Form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['full_name', 'email_id', 'address']

class Update_Product_Form(forms.ModelForm):
    class Meta:
        product_image = forms.ImageField(required=False)
        model = Products
        fields = ['product_name', 'product_image', 'description', 'stock', 'availability', 'price']


class Update_Home_images(forms.ModelForm):
    class Meta:
        Image1 = forms.ImageField(required=False)
        Image2 = forms.ImageField(required=False)
        Image3 = forms.ImageField(required=False)
        model = Home_page_images
        fields = ['Image1', 'Image2', 'Image3']
