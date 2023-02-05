from django import forms

class TodoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    done = forms.BooleanField(required=False)

class ContactForm(forms.Form):
    name = forms.CharField(label="Imię")
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

