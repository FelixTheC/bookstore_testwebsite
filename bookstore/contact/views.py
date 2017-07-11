from django.contrib.messages import success
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ContactMailForm

class ContactFormView(FormView):
    form_class = ContactMailForm
    template_name = 'contact_contact.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['form'] = ContactMailForm
        return context

    def post(self, request, *args, **kwargs):
        context_form = self.form_class(data=request.POST)
        print(kwargs)
        if context_form.is_valid():
            send_mail(
                subject=request.POST.get('emailSubject', ''),
                from_email=request.POST.get('emailAddresse', ''),
                message=request.POST.get('emailContent', ''),
                recipient_list=['fberndt87@gmail.com', ],
                fail_silently=False
            )
            return redirect('store:book_main')
        return render(request, 'contact_contact.html', context={'form': self.form_class})
