from .models import Todo
from django import forms


class CreateTodoForm(forms.Form):
    title = forms.CharField(label="عنوان")
    text = forms.CharField(widget=forms.Textarea, label="متن")
    is_active = forms.BooleanField(widget=forms.CheckboxInput(), label='فعال بودن')
    def create_todo(self, user):
        cd = self.cleaned_data
        Todo.objects.create(
            title=cd["title"], text=cd["text"], user=user
        )
