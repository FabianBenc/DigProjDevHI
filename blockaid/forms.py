from django import forms
from .models import Color
from .models import Product

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['torso_color','pockets_color','left_sleeve_color','right_sleeve_color']

class IsInShopForm(forms.Form):
    color_id = forms.CharField(max_length=255)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'colors']
        widgets = {'colors': forms.HiddenInput()}

