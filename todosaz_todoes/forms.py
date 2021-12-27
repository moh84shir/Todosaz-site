from .models import Todo
from django.contrib.auth.models import User
from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(label="عنوان")
    simple_desc = forms.CharField(label="توضیحات کوتاه")
    text = forms.CharField(widget=forms.Textarea, label="متن")

    def create_todo(self, user):
        cd = self.cleaned_data
        Todo.objects.create(
            title=cd["title"], simple_desc=cd["simple_desc"], text=cd["text"], user=user
        )
