from django import forms
from forum.models import Advertisement

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('user',)
