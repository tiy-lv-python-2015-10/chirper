from django import forms
from django.forms import Textarea
from chirp.models import Chirp


class ChirpForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ('title', 'message')
        widgets = {
            'message': Textarea(attrs={'rows': 2})
        }
