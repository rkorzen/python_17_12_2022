
from django import forms
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from django.contrib import admin
from posts.models import Post
from tags.models import Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=AutocompleteSelectMultiple(
            Post._meta.get_field("tags"),
            admin.AdminSite()
        )
    )

    class Meta:
        model = Post
        fields = ["title", "content", "img", "datafile", "tags"]

