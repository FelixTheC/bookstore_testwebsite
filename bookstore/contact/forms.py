from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import mail_managers, BadHeaderError


class ContactMailForm(forms.Form):
    CHOICES = (
        ('Feedback', 'Feedback'),
        ('Support', 'Support'),
        ('Ohne Betreff', 'Ohne Betreff'),
    )
    emailSubject = forms.ChoiceField(choices=CHOICES,
                                     label='Grund',
                                     initial=1,)
    emailAddresse = forms.EmailField(label='Email Addresse',
                                     required=True,
                                     help_text='yourEmail@help.com')
    emailContent = forms.CharField(label='Ihre Nachricht', widget=forms.Textarea)
