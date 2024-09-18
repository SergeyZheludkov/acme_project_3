from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label='Name', max_length=20)
    last_name = forms.CharField(
        label='Surname', required=False, help_text='Optional field'
    )
    birthday = forms.DateField(
        label='Birthday',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
