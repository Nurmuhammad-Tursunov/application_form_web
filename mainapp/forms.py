from django.forms import ModelForm
from mainapp.models import Application
from django import forms


class ApplicationForm(ModelForm):
    photo = forms.FileField(required=False)

    class Meta:
        model = Application
        fields = (
            # 'city',
            'first_name',
            'last_name',
            'phone_number',
            # 'date_of_birth',
            # 'position',
            # 'degree',
            # 'address',
            # 'language_ru',
            # 'computer_science',
            'photo',
            # 'appeal',
        )
