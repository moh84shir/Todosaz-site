from django import forms
from .models import New


class CreateNewForm(forms.Form):
    title = forms.CharField(label="عنوان")
    subject = forms.CharField(label="موضوع")
    text = forms.CharField(widget=forms.Textarea, label="متن")

    def create_new(self):
        cd = self.cleaned_data
        New.objects.create(
            title=cd["title"],
            subject=cd["subject"],
            text=cd["text"],
        )
