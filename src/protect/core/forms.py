from django import forms

from protect.core.models import Person


class DateInput(forms.DateInput):
    input_type = 'date'


class ReportForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'first_name', 'last_name', 'nickname', 'place', 'date', 'photo', 'comment_photo', 'age',
                  'gender', 'detail', 'type_publication']
        widgets = {
            'date': DateInput()
        }
