from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class BookForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
    year = forms.IntegerField()


    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    # helper.form_method = 'POST'