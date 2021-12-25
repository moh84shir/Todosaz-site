from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label="نام شریفتان", max_length=50)
    email = forms.EmailField(label="ایمیل شما", max_length=120)
    title = forms.CharField(label="عنوان پیام", max_length=50)
    subject = forms.CharField(label="موضوع پیامتان", max_length=80)
    text = forms.CharField(label="متن پیامتان", widget=forms.Textarea)

    def send_mail(self):
        cd = self.cleaned_data
        contact_message = f"""
                سلام محمد عزیز
                دوستتان {cd['name']} برای شما پیغامی دارد که به شرح زیر است : 
                {cd['title']}

                {cd['text']}

                ایمیل : {cd['email']}
            """

        send_mail(
            subject=cd['subject'],
            message=contact_message,
            from_email='chertandpert120@gmail.com',
            recipient_list=['chertandpert120@gmail.com'],
        )
