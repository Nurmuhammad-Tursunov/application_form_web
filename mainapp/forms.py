from django.forms import ModelForm
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
            # 'degree',
            'family',
            'address',
            # 'languages',
            'last_work',
            'last_position',
            'work_time',
            'computer_science',
            'photo',

            # 'father_name',
            # 'phone_number2',
            'appeal',
            'about',
                  )

        # extra_kwargs = {
        #     'father_name': {'required': False},
        #     'phone_number2': {'required': False},
        #     'appeal': {'required': False},
        #     'about': {'required': False},
        # }
