from django import forms
from .models import Csv

class ContactForm(forms.Form):
    x_axis = forms.ChoiceField(choices =[('age', 'Age'), ('gender', 'Gender'), ('accent', 'Accent')])
    y_axis = forms.ChoiceField(choices =[('age', 'Age'), ('gender', 'Gender'), ('accent', 'Accent')])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)



