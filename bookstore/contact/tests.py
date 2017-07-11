from django.test import TestCase
from .forms import ContactMailForm

# Create your tests here.
class ContactFormTest(TestCase):

    def setUp(self):
        pass

    def test_valid_form(self):
        subject = 'Support'
        addresse = 'fberndt87@gmail.com'
        content = "'Ganz viel\n Text'"
        data = {'emailSubject': subject,
                'emailAddresse': addresse,
                'emailContent': content}
        form = ContactMailForm(data=data)
        self.assertTrue(form.is_valid())


    def test_invalid_subject_form(self):
        subject = ''
        addresse = 'fberndt87@gmail.com'
        content = 'Ganz viel Text'
        data = {'emailSubject': subject,
                'emailAddresse': addresse,
                'emailContent': content}
        form = ContactMailForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_email_form(self):
        subject = 'Support'
        addresse = 'f@.com'
        content = 'Ganz viel Text'
        data = {'emailSubject': subject,
                'emailAddresse': addresse,
                'emailContent': content}
        form = ContactMailForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_content_form(self):
        subject = 'Feedback'
        addresse = 'fberndt87@gmail.com'
        content = ' '
        data = {'emailSubject': subject,
                'emailAddresse': addresse,
                'emailContent': content}
        form = ContactMailForm(data=data)
        self.assertFalse(form.is_valid())
