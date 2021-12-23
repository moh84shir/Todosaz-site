from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from .forms import ContactForm


class Contact(FormView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact/contact.html'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
