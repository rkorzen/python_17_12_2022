from django import forms


class TodoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    done = forms.BooleanField(required=False)


TodoFormset = forms.formset_factory(TodoForm, extra=3)
