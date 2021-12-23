from django import forms
from .models import New


class CreateNewForm(forms.Form):
    title = forms.CharField(label="عنوان")
    subject = forms.CharField(label="موضوع")
    short_desc = forms.CharField(label="توضیح کوتاه")
    text = forms.CharField(widget=forms.Textarea, label="متن")
    is_active = forms.BooleanField(label="فعال  است/نیست")

    def create_new(self):
        cd = self.cleaned_data
        New.objects.create(
            title=cd["title"],
            subject=cd["subject"],
            text=cd["text"],
            is_active=cd["is_active"],
            short_desc=cd["short_desc"],
        )
