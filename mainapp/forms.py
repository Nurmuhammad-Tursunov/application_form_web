from django.forms import ModelForm
from django import forms
from mainapp.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = (
            'region',
            'city',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'position',
            'degree',
            'family',
            'address',
            'languages',
            'last_work',
            'last_position',
            'work_time',
            'computer_science',
            'photo',

            'father_name',
            'phone_number2',
            'appeal',
            'about',
                  )
        # fields = "__all__"
        extra_kwargs = {
            'father_name': {'required': False},
            'phone_number2': {'required': False},
            'appeal': {'required': False},
            'about': {'required': False},
        }


class ApplicationForm2(forms.Form):
    photo = forms.FileField()
    region = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    father_name = forms.CharField(max_length=255, required=False)
    phone_number2 = forms.CharField(max_length=255, required=False)
    appeal = forms.CharField(max_length=255, required=False)
    university = forms.CharField(max_length=255, required=False)
    about = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    position = forms.IntegerField()
    degree = forms.IntegerField()
    family = forms.IntegerField(required=False)
    address = forms.CharField(max_length=500)
    languages = forms.CharField(max_length=255)
    last_work = forms.CharField(max_length=255)
    last_position = forms.CharField(max_length=255)
    work_time = forms.CharField(max_length=255)
    computer_science = forms.IntegerField()
