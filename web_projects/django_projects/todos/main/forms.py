from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Imię")
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)