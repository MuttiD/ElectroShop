from django.shortcuts import render
from django.views.generic import CreateView, View, FormView
from .forms import ContactForm


class ContactView(FormView):
    """"
    A class based view to render Contacts
    """
    form_class = ContactForm
    template_name = 'contact_us.html'
    success_url = '/success'

    def get(self, request):
        form = ContactForm()
        return render(request, 'contact_us.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'contact_us.html', {'form': form})


def success(request):
    """
    A view to render the success of a contact submitted
    """
    return render(request, 'success.html')
