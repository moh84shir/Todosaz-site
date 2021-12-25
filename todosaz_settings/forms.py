from django import forms
from .models import Setting


class ChangeSettingsFrom(forms.Form):
    title = forms.CharField(label="عنوان")
    short_desc = forms.CharField(label="توضیحات کوتاه")
    about = forms.CharField(
        widget=forms.Textarea(attrs={"class": ""}),
        label="درباره ی سایت",
    )
    email = forms.EmailField(label="ایمیل")
    phone = forms.CharField(label="تلفن تماس")

    def change_settings(self):
        cd = self.cleaned_data
        try:
            settings = Setting.objects.last()
            settings.title = cd["title"] if "title" in cd else settings.title
            settings.short_desc = (
                cd["short_desc"] if "short_desc" in cd else settings.short_desc
            )
            settings.about = cd["about"] if "about" in cd else settings.about
            settings.email = cd["email"] if "email" in cd else settings.email
            settings.phone = cd["phone"] if "phone" in cd else settings.phone
            settings.save()
        except:
            Setting.objects.create(
                title="", short_desc="", about="", email="", phone=""
            )
