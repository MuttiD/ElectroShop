from django.shortcuts import render
from django.views.generic import CreateView, View, FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm


class ContactView(SuccessMessageMixin, FormView):
    """"
    A class based view to render Contacts
    """
    form_class = ContactForm
    template_name = 'contactUs/contact_us.html'
    success_url = '/'
    success_message = "Thanks for contacting us. We will reply to you shortly"

    def get(self, request):
        form = ContactForm()
        return render(request, 'contactUs/contact_us.html', {'form': form})
