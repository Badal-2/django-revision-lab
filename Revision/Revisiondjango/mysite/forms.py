from django import forms
from .models import *

from django.core.validators import FileExtensionValidator


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"


        
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']



    # Example validators: only allow jpg/jpeg/png and limit size to 5MB
    def clean_image(self):
        img = self.cleaned_data.get('image')
        if img:
            # File extension validator (add more extensions if needed)
            valid_ext = ['jpg','jpeg','png','gif']
            ext = img.name.split('.')[-1].lower()
            if ext not in valid_ext:
                raise forms.ValidationError('Unsupported file extension.')

            # Size check (5MB)
            if img.size > 5 * 1024 * 1024:
                raise forms.ValidationError('File too large (max 5MB).')
        return img






