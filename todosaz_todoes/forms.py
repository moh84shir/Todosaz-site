from .models import Todo
from django.contrib.auth.models import User
from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField()
    simple_desc = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def create_todo(self, user):
        cd = self.cleaned_data
        Todo.objects.create(
            title=cd["title"], simple_desc=cd["simple_desc"], text=cd["text"], user=user
        )
