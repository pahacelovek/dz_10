from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 3:
            raise ValidationError('Название должно быть не короче 3 символов')
        elif data[0] == '?':
            raise ValidationError('Название не может начинаться с символа "?"')
        return data

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
        }

# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#
#     auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
#
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
