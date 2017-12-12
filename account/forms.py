from django.forms import ModelForm, Form, CheckboxSelectMultiple
from .models import Profile

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'schools', 'degrees', 'program', 'grad_year',
            'resume', 'viewable'
        ]
        widgets = {
            'schools': CheckboxSelectMultiple(),
            'degrees': CheckboxSelectMultiple(),
        }
