from django import forms
from .models import Color

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['torso_color','pockets_color','left_sleeve_color','right_sleeve_color']